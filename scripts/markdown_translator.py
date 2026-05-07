#!/usr/bin/env python3
"""
Professional Markdown Translation System using DashScope API.

Translates markdown files to Chinese using type-specific prompts for optimal quality.
Processes all markdown files in the repository (excluding vi/, zh/, .claude/) and
saves translations as file_ZH.md next to original files.

Features: type-aware translation, parallel processing, comprehensive logging,
error handling with retry logic, resume capability.

Usage:
    python scripts/markdown_translator.py
    python scripts/markdown_translator.py --verbose --concurrent 5
    nohup python scripts/markdown_translator.py --log-dir ./logs &
"""

import argparse
import asyncio
import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import httpx


class TranslationLogger:
    """Multi-level logging system with progress tracking for resume capability."""

    def __init__(self, log_dir: Path, verbose: bool = False):
        self.log_dir = log_dir
        self.log_dir.mkdir(exist_ok=True)

        self.translation_log = self.log_dir / "translation.log"
        self.error_log = self.log_dir / "errors.log"
        self.api_log = self.log_dir / "api_calls.log"
        self.progress_log = self.log_dir / "progress.json"

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        self.trans_logger = logging.getLogger("translation")
        self.trans_logger.setLevel(logging.DEBUG if verbose else logging.INFO)
        trans_handler = logging.FileHandler(self.translation_log)
        trans_handler.setFormatter(formatter)
        self.trans_logger.addHandler(trans_handler)

        self.error_logger = logging.getLogger("errors")
        self.error_logger.setLevel(logging.ERROR)
        error_handler = logging.FileHandler(self.error_log)
        error_handler.setFormatter(formatter)
        self.error_logger.addHandler(error_handler)

        self.api_logger = logging.getLogger("api")
        self.api_logger.setLevel(logging.DEBUG)
        api_handler = logging.FileHandler(self.api_log)
        api_handler.setFormatter(formatter)
        self.api_logger.addHandler(api_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.trans_logger.addHandler(console_handler)

    def info(self, message: str):
        self.trans_logger.info(message)

    def error(self, message: str, exc_info: bool = False):
        self.error_logger.error(message, exc_info=exc_info)
        self.trans_logger.error(message)

    def debug(self, message: str):
        self.trans_logger.debug(message)
        self.api_logger.debug(message)

    def api_call(self, request: dict, response: dict, duration: float):
        self.api_logger.debug(f"API Request: {json.dumps(request, ensure_ascii=False)}")
        self.api_logger.debug(
            f"API Response: {json.dumps(response, ensure_ascii=False)}"
        )
        self.api_logger.debug(f"API Duration: {duration:.2f}s")

    def save_progress(
        self, completed: List[str], failed: List[str], in_progress: Optional[str] = None
    ):
        progress = {
            "timestamp": datetime.now().isoformat(),
            "completed": completed,
            "failed": failed,
            "in_progress": in_progress,
            "total_completed": len(completed),
            "total_failed": len(failed),
        }
        with open(self.progress_log, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2, ensure_ascii=False)

    def load_progress(self) -> Tuple[List[str], List[str]]:
        if not self.progress_log.exists():
            return [], []

        try:
            with open(self.progress_log, "r", encoding="utf-8") as f:
                progress = json.load(f)
                return progress.get("completed", []), progress.get("failed", [])
        except Exception as e:
            self.error(f"Failed to load progress: {e}")
            return [], []


class MarkdownTranslator:
    """Core translation engine with type-specific prompts for optimal quality."""

    def __init__(self, api_key: str, logger: TranslationLogger, timeout: int = 120):
        self.api_key = api_key
        self.logger = logger
        self.timeout = timeout
        self.base_url = "https://dashscope.aliyuncs.com/api/v1"
        self.model = "qwen-plus"
        self.prompt_templates = self._init_prompt_templates()

    def _init_prompt_templates(self) -> Dict[str, str]:
        return {
            "main_docs": """You are a professional technical documentation translator.

Task: Translate English markdown to professional, easy-to-understand Chinese.

Style Guidelines:
- Clear, welcoming language for developers
- Professional yet approachable tone
- Preserve markdown formatting, links, code blocks
- Accurate, consistent technical terms
- Natural Chinese flow, avoid literal translations
- Maintain section structure and hierarchy

Target Audience: Chinese-speaking developers and technical users

Output: Return ONLY the translated markdown content, no explanations.
""",
            "module_readme": """You are a technical education content translator.

Task: Translate English module documentation to structured, educational Chinese.

Style Guidelines:
- Instructional tone with clear learning progression
- Consistent terminology for technical concepts
- Preserve all code examples, commands, file paths
- Maintain numbered lists, bullet points, section hierarchy
- Explain concepts clearly for intermediate learners
- Keep URLs, file names, and code comments in English
- Natural Chinese that flows well for tutorials

Target Audience: Chinese developers learning Claude Code features

Output: Return ONLY the translated markdown content, no explanations.
""",
            "slash_command": """You are a technical command documentation translator.

Task: Translate English slash command documentation to concise, action-oriented Chinese.

Style Guidelines:
- Direct, practical tone focused on usage
- Keep command names, parameters, and code examples unchanged
- Clear, imperative language for instructions
- Preserve markdown tables, code blocks, and syntax
- Maintain consistency with existing command documentation
- Use immediately actionable Chinese

Target Audience: Chinese developers using Claude Code commands

Output: Return ONLY the translated markdown content, no explanations.
""",
            "skill_docs": """You are a technical specification translator.

Task: Translate English skill documentation to precise, detailed Chinese.

Style Guidelines:
- Precise, technical tone with exact terminology
- Preserve all configuration examples, JSON/YAML structures
- Keep file paths, environment variables, and code snippets unchanged
- Maintain clear specification format with examples
- Use consistent technical vocabulary
- Explain configuration options clearly

Target Audience: Chinese developers configuring Claude Code skills

Output: Return ONLY the translated markdown content, no explanations.
""",
            "config_examples": """You are a technical code-commentary translator.

Task: Translate English configuration documentation to explanatory Chinese.

Style Guidelines:
- Mix of technical accuracy and explanatory clarity
- Keep all code blocks, JSON, YAML, and configuration syntax unchanged
- Translate comments and explanatory text only
- Preserve file structures and formatting
- Explain "why" not just "what"
- Maintain balance between code and commentary

Target Audience: Chinese developers implementing configurations

Output: Return ONLY the translated markdown content, no explanations.
""",
        }

    def categorize_file(self, file_path: Path) -> str:
        path_str = str(file_path)
        file_name = file_path.name

        if file_name in [
            "README.md",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "STYLE_GUIDE.md",
            "LEARNING-ROADMAP.md",
            "INDEX.md",
            "CATALOG.md",
            "QUICK_REFERENCE.md",
            "SECURITY.md",
            "RELEASE_NOTES.md",
        ]:
            return "main_docs"

        if "/01-slash-commands/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/02-memory/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/03-skills/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/04-subagents/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/05-mcp/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/06-hooks/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/07-plugins/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/08-checkpoints/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/09-advanced-features/" in path_str and file_name == "README.md":
            return "module_readme"
        if "/10-cli/" in path_str and file_name == "README.md":
            return "module_readme"

        if "/01-slash-commands/" in path_str and file_name != "README.md":
            return "slash_command"

        if "/03-skills/" in path_str and "SKILL.md" in file_name:
            return "skill_docs"

        if any(pattern in path_str for pattern in ["config", "example", "template"]):
            return "config_examples"

        return "main_docs"

    async def translate_markdown(self, content: str, category: str) -> str:
        if category not in self.prompt_templates:
            category = "main_docs"

        system_prompt = self.prompt_templates[category]
        user_prompt = f"""Translate the following markdown content to Chinese:

--- BEGIN CONTENT ---
{content}
--- END CONTENT ---

Return ONLY the translated markdown, no explanations."""

        payload = {
            "model": self.model,
            "input": {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            },
            "parameters": {
                "result_format": "message",
                "temperature": 0.3,
                "top_p": 0.9,
            },
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        start_time = time.time()

        try:
            async with httpx.AsyncClient(
                timeout=httpx.Timeout(10.0, read=self.timeout)
            ) as client:
                response = await client.post(
                    f"{self.base_url}/services/aigc/text-generation/generation",
                    json=payload,
                    headers=headers,
                )

                duration = time.time() - start_time

                if response.status_code != 200:
                    self.logger.error(
                        f"API error: {response.status_code} - {response.text}"
                    )
                    raise Exception(f"API request failed: {response.status_code}")

                result = response.json()
                self.logger.api_call(payload, result, duration)

                if "output" in result and "choices" in result["output"]:
                    translated = result["output"]["choices"][0]["message"]["content"]
                    return translated.strip()
                else:
                    self.logger.error(f"Unexpected API response format: {result}")
                    raise Exception("Invalid API response format")

        except httpx.TimeoutException as e:
            self.logger.error(
                f"Translation failed: {type(e).__name__} after {self.timeout}s",
                exc_info=True,
            )
            raise
        except Exception as e:
            self.logger.error(f"Translation failed: {e!r}", exc_info=True)
            raise

    async def translate_file(
        self, file_path: Path, output_path: Path, category: str
    ) -> bool:
        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                self.logger.info(f"Translating: {file_path} (attempt {attempt + 1})")

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                translated = await self.translate_markdown(content, category)

                if not translated or len(translated.strip()) < len(content) * 0.1:
                    raise Exception(
                        "Translation output seems too short, possible error"
                    )

                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(translated)

                self.logger.info(f"✅ Successfully translated: {file_path}")
                return True

            except Exception as e:
                self.logger.error(f"Attempt {attempt + 1} failed for {file_path}: {e}")

                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2**attempt)
                    self.logger.info(f"Retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    self.logger.error(
                        f"❌ Failed after {max_retries} attempts: {file_path}"
                    )
                    return False

        return False


class BatchTranslator:
    """Orchestrates parallel translation with concurrency control and progress tracking."""

    def __init__(
        self,
        translator: MarkdownTranslator,
        logger: TranslationLogger,
        concurrent: int = 5,
        resume: bool = True,
    ):
        self.translator = translator
        self.logger = logger
        self.concurrent = concurrent
        self.resume = resume

    def discover_files(self, root_path: Path) -> List[Path]:
        exclude_patterns = [
            "vi/",
            "zh/",
            ".claude/",
            ".git/",
            "node_modules/",
            "__pycache__/",
        ]

        md_files = []
        for md_file in root_path.rglob("*.md"):
            path_str = str(md_file)

            if any(pattern in path_str for pattern in exclude_patterns):
                continue

            if md_file.name.endswith("_ZH.md"):
                continue

            zh_file = md_file.parent / f"{md_file.stem}_ZH.md"
            if zh_file.exists():
                self.logger.debug(f"Skipping (already translated): {md_file}")
                continue

            md_files.append(md_file)

        self.logger.info(f"Found {len(md_files)} files to translate")
        return sorted(md_files)

    async def process_batch(
        self, files: List[Path], root_path: Path
    ) -> Tuple[int, int]:
        semaphore = asyncio.Semaphore(self.concurrent)

        completed_files, failed_files = (
            self.logger.load_progress() if self.resume else ([], [])
        )
        completed_set = set(completed_files)
        failed_set = set(failed_files)

        self.logger.info(
            f"Resuming: {len(completed_set)} completed, {len(failed_set)} failed"
        )

        async def process_file(md_file: Path) -> Tuple[bool, str]:
            async with semaphore:
                file_id = str(md_file.relative_to(root_path))

                if file_id in completed_set:
                    self.logger.debug(f"Skipping completed: {file_id}")
                    return True, file_id

                category = self.translator.categorize_file(md_file)
                self.logger.debug(f"Categorized {file_id} as: {category}")

                output_path = md_file.parent / f"{md_file.stem}_ZH.md"
                success = await self.translator.translate_file(
                    md_file, output_path, category
                )

                return success, file_id

        tasks = [
            process_file(f)
            for f in files
            if str(f.relative_to(root_path)) not in completed_set
        ]

        if not tasks:
            self.logger.info("No new files to process")
            return len(completed_set), len(failed_set)

        self.logger.info(
            f"Processing {len(tasks)} files with concurrency {self.concurrent}"
        )

        completed = list(completed_set)
        failed = list(failed_set)

        for i, coro in enumerate(asyncio.as_completed(tasks), 1):
            try:
                success, file_id = await coro

                if success:
                    completed.append(file_id)
                    self.logger.info(f"Progress: {i}/{len(tasks)} - ✅ {file_id}")
                else:
                    failed.append(file_id)
                    self.logger.info(f"Progress: {i}/{len(tasks)} - ❌ {file_id}")

                if i % 5 == 0:
                    self.logger.save_progress(completed, failed)

            except Exception as e:
                self.logger.error(
                    f"Unexpected error processing file: {e}", exc_info=True
                )

        self.logger.save_progress(completed, failed)

        return len(completed), len(failed)


async def main():
    parser = argparse.ArgumentParser(
        description="Professional Markdown Translation System using DashScope API"
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=Path.cwd(),
        help="Root directory to process (default: current directory)",
    )
    parser.add_argument(
        "--concurrent",
        "-c",
        type=int,
        default=5,
        help="Number of concurrent translations (default: 5)",
    )
    parser.add_argument(
        "--log-dir",
        "-l",
        type=Path,
        default=Path("logs"),
        help="Log directory (default: ./logs)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Start fresh without resuming previous progress",
    )
    parser.add_argument(
        "--timeout", type=int, default=120, help="API timeout in seconds (default: 120)"
    )

    args = parser.parse_args()

    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        print("❌ Error: DASHSCOPE_API_KEY environment variable not set")
        print("Please set it: export DASHSCOPE_API_KEY='your-api-key'")
        return 1

    logger = TranslationLogger(args.log_dir, args.verbose)
    logger.info("=" * 60)
    logger.info("🌏 Markdown Translation System Starting")
    logger.info("=" * 60)
    logger.info(f"Root directory: {args.root}")
    logger.info(f"Concurrent workers: {args.concurrent}")
    logger.info(f"Resume enabled: {not args.no_resume}")

    translator = MarkdownTranslator(api_key, logger, args.timeout)
    batch_translator = BatchTranslator(
        translator, logger, args.concurrent, not args.no_resume
    )

    logger.info("🔍 Discovering markdown files...")
    files_to_translate = batch_translator.discover_files(args.root)

    if not files_to_translate:
        logger.info("No files to translate. Exiting.")
        return 0

    start_time = time.time()
    logger.info(f"🚀 Starting translation of {len(files_to_translate)} files")

    try:
        completed, failed = await batch_translator.process_batch(
            files_to_translate, args.root
        )

        elapsed = time.time() - start_time
        logger.info("=" * 60)
        logger.info("📊 Translation Complete")
        logger.info("=" * 60)
        logger.info(f"✅ Successfully translated: {completed} files")
        logger.info(f"❌ Failed: {failed} files")
        logger.info(f"⏱️  Total time: {elapsed:.2f} seconds")
        logger.info(f"📁 Log files: {args.log_dir}/")

        if failed > 0:
            logger.info(f"\nCheck {args.log_dir}/errors.log for details")

        return 0 if failed == 0 else 1

    except KeyboardInterrupt:
        logger.info("\n🛑 Translation interrupted by user")
        return 130
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
