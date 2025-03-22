"""Black code formatting module."""

import os
from typing import Any, Dict, List, Optional, Set, Union
from pathlib import Path
import black
from black import FileMode, InvalidInput
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn


# Initialize Rich console
console = Console()


class BlackFormatter:
    """Manager for Black code formatting."""

    def __init__(
        self,
        line_length: int = 88,
        target_versions: Optional[Set[black.TargetVersion]] = None,
        include: Optional[str] = None,
        exclude: Optional[str] = None,
        force_exclude: Optional[str] = None,
        preview: bool = False,
        quiet: bool = False
    ):
        """Initialize the formatter.

        Args:
            line_length: Maximum line length
            target_versions: Python versions to target
            include: Include pattern for files
            exclude: Exclude pattern for files
            force_exclude: Force exclude pattern for files
            preview: Enable preview mode
            quiet: Suppress output
        """
        self.line_length = line_length
        self.target_versions = target_versions or {black.TargetVersion.PY37}
        self.include = include
        self.exclude = exclude
        self.force_exclude = force_exclude
        self.preview = preview
        self.quiet = quiet
        self.mode = FileMode(
            target_versions=self.target_versions,
            line_length=self.line_length,
            string_normalization=True,
            is_pyi=False,
            is_ipynb=False,
            skip_source_first_line=False,
            preview=self.preview
        )

    def format_file(
        self,
        file_path: Union[str, Path],
        check: bool = False,
        diff: bool = False
    ) -> bool:
        """Format a single file.

        Args:
            file_path: Path to the file
            check: Check if file is formatted without making changes
            diff: Show diff instead of making changes

        Returns:
            bool: True if formatting was successful
        """
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                console.print(f"[red]File not found: {file_path}[/]")
                return False

            if check:
                return black.format_file_in_place(
                    file_path,
                    fast=False,
                    mode=self.mode,
                    write_back=black.WriteBack.NO
                )

            if diff:
                diff_content = black.format_file_in_place(
                    file_path,
                    fast=False,
                    mode=self.mode,
                    write_back=black.WriteBack.DIFF
                )
                if diff_content:
                    console.print(f"[yellow]Changes for {file_path}:[/]")
                    console.print(diff_content)
                return True

            return black.format_file_in_place(
                file_path,
                fast=False,
                mode=self.mode,
                write_back=black.WriteBack.YES
            )

        except InvalidInput as e:
            console.print(f"[red]Invalid input in {file_path}: {e}[/]")
            return False
        except Exception as e:
            console.print(f"[red]Error formatting {file_path}: {e}[/]")
            return False

    def format_directory(
        self,
        directory: Union[str, Path],
        check: bool = False,
        diff: bool = False
    ) -> Dict[str, bool]:
        """Format all Python files in a directory.

        Args:
            directory: Directory to format
            check: Check if files are formatted without making changes
            diff: Show diff instead of making changes

        Returns:
            Dict[str, bool]: Dictionary mapping file paths to success status
        """
        directory = Path(directory)
        if not directory.exists():
            console.print(f"[red]Directory not found: {directory}[/]")
            return {}

        results = {}
        python_files = list(directory.rglob("*.py"))

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(
                "Formatting files...",
                total=len(python_files)
            )

            for file_path in python_files:
                if self._should_format_file(file_path):
                    success = self.format_file(
                        file_path,
                        check=check,
                        diff=diff
                    )
                    results[str(file_path)] = success
                progress.advance(task)

        return results

    def _should_format_file(self, file_path: Path) -> bool:
        """Check if a file should be formatted.

        Args:
            file_path: Path to the file

        Returns:
            bool: True if file should be formatted
        """
        if self.include and not black.re_compile_maybe_verbose(self.include).search(
            str(file_path)
        ):
            return False

        if self.exclude and black.re_compile_maybe_verbose(self.exclude).search(
            str(file_path)
        ):
            return False

        if self.force_exclude and black.re_compile_maybe_verbose(
            self.force_exclude
        ).search(str(file_path)):
            return False

        return True

    def display_results(self, results: Dict[str, bool]) -> None:
        """Display formatting results in a formatted table.

        Args:
            results: Dictionary mapping file paths to success status
        """
        table = Table(title="Formatting Results")
        table.add_column("File", style="cyan")
        table.add_column("Status", style="green")

        for file_path, success in results.items():
            status = "✓" if success else "✗"
            style = "green" if success else "red"
            table.add_row(file_path, f"[{style}]{status}[/]")

        console.print(table)

    def create_config_file(self, config_path: Union[str, Path] = "pyproject.toml") -> None:
        """Create a Black configuration file.

        Args:
            config_path: Path to save the configuration file
        """
        config = {
            "tool": {
                "black": {
                    "line-length": self.line_length,
                    "target-version": [v.name for v in self.target_versions],
                    "include": self.include,
                    "exclude": self.exclude,
                    "force-exclude": self.force_exclude,
                    "preview": self.preview
                }
            }
        }

        try:
            import tomli_w
            with open(config_path, 'w') as f:
                tomli_w.dump(config, f)
            console.print(f"[green]Created configuration file: {config_path}[/]")

        except Exception as e:
            console.print(f"[red]Error creating config file: {e}[/]")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize formatter
        formatter = BlackFormatter(
            line_length=88,
            include=r"\.pyi?$",
            exclude=r"/(\.git|\.hg|\.mypy_cache|\.tox|\.venv|_build|buck-out|build|dist)/"
        )

        # Create configuration file
        formatter.create_config_file()

        # Format a single file
        console.print("\n[bold]Formatting single file...[/]")
        success = formatter.format_file("example.py")
        console.print(f"Formatting {'successful' if success else 'failed'}")

        # Format a directory
        console.print("\n[bold]Formatting directory...[/]")
        results = formatter.format_directory(".")
        formatter.display_results(results)

        # Check formatting without making changes
        console.print("\n[bold]Checking formatting...[/]")
        results = formatter.format_directory(".", check=True)
        formatter.display_results(results)

        # Show diff without making changes
        console.print("\n[bold]Showing diff...[/]")
        formatter.format_file("example.py", diff=True)

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 