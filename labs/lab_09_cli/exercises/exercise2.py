"""CLI tool development module with interactive features."""

import os
import sys
from typing import Any, Dict, List, Optional, Union
import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter


# Initialize Rich console
console = Console()


class CLITool:
    """Base class for CLI tools with interactive features."""

    def __init__(
        self,
        name: str,
        description: str,
        history_file: Optional[str] = None
    ):
        """Initialize the CLI tool.

        Args:
            name: Tool name
            description: Tool description
            history_file: Path to command history file
        """
        self.name = name
        self.description = description
        self.history_file = history_file or f".{name}_history"
        self.session = PromptSession(
            history=FileHistory(self.history_file),
            auto_suggest=AutoSuggestFromHistory()
        )
        self.commands: Dict[str, callable] = {}

    def register_command(self, name: str, func: callable) -> None:
        """Register a command handler.

        Args:
            name: Command name
            func: Command handler function
        """
        self.commands[name] = func

    def show_help(self) -> None:
        """Display help information."""
        table = Table(title=f"{self.name} - {self.description}")
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")

        for name, func in self.commands.items():
            table.add_row(name, func.__doc__ or "No description available")

        console.print(table)

    def show_progress(self, description: str, total: int = 100) -> Progress:
        """Create a progress bar.

        Args:
            description: Progress description
            total: Total number of steps

        Returns:
            Progress: Progress bar instance
        """
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        )

    def show_spinner(self, description: str) -> Progress:
        """Create a spinner for indeterminate progress.

        Args:
            description: Spinner description

        Returns:
            Progress: Spinner instance
        """
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        )

    def show_table(
        self,
        title: str,
        columns: List[str],
        rows: List[List[Any]]
    ) -> None:
        """Display data in a table.

        Args:
            title: Table title
            columns: Column names
            rows: Table rows
        """
        table = Table(title=title)
        for col in columns:
            table.add_column(col)

        for row in rows:
            table.add_row(*[str(cell) for cell in row])

        console.print(table)

    def show_panel(self, content: str, title: Optional[str] = None) -> None:
        """Display content in a panel.

        Args:
            content: Panel content
            title: Panel title
        """
        console.print(Panel(content, title=title))

    def prompt(
        self,
        question: str,
        default: Optional[str] = None,
        choices: Optional[List[str]] = None
    ) -> str:
        """Display an interactive prompt.

        Args:
            question: Prompt question
            default: Default value
            choices: List of valid choices

        Returns:
            str: User input
        """
        if choices:
            return Prompt.ask(
                question,
                default=default,
                choices=choices,
                show_choices=True
            )
        return Prompt.ask(question, default=default)

    def confirm(self, question: str, default: bool = True) -> bool:
        """Display a confirmation prompt.

        Args:
            question: Confirmation question
            default: Default value

        Returns:
            bool: User confirmation
        """
        return Confirm.ask(question, default=default)

    def interactive_shell(self) -> None:
        """Start an interactive shell."""
        console.print(f"[bold blue]Welcome to {self.name}![/]")
        console.print(f"[italic]{self.description}[/]")
        console.print("Type 'help' for available commands or 'exit' to quit.\n")

        while True:
            try:
                command = self.session.prompt(f"{self.name}> ")
                command = command.strip()

                if command.lower() in ('exit', 'quit'):
                    break
                elif command.lower() == 'help':
                    self.show_help()
                elif command in self.commands:
                    try:
                        self.commands[command]()
                    except Exception as e:
                        console.print(f"[red]Error: {e}[/]")
                else:
                    console.print(f"[yellow]Unknown command: {command}[/]")

            except KeyboardInterrupt:
                continue
            except EOFError:
                break


# Example CLI tool implementation
class FileManager(CLITool):
    """Example CLI tool for file management."""

    def __init__(self):
        """Initialize the file manager."""
        super().__init__(
            name="filemanager",
            description="A simple file management tool"
        )
        self.register_command("list", self.list_files)
        self.register_command("create", self.create_file)
        self.register_command("delete", self.delete_file)
        self.register_command("info", self.file_info)

    def list_files(self) -> None:
        """List files in the current directory."""
        with self.show_progress("Listing files...") as progress:
            task = progress.add_task("Scanning directory...", total=None)
            files = os.listdir(".")
            progress.update(task, completed=True)

        rows = []
        for file in files:
            stat = os.stat(file)
            rows.append([
                file,
                "Directory" if os.path.isdir(file) else "File",
                f"{stat.st_size:,} bytes",
                stat.st_mtime
            ])

        self.show_table(
            "Files in Current Directory",
            ["Name", "Type", "Size", "Modified"],
            rows
        )

    def create_file(self) -> None:
        """Create a new file."""
        filename = self.prompt("Enter filename")
        content = self.prompt("Enter file content")

        with self.show_progress("Creating file...", total=100) as progress:
            task = progress.add_task("Writing file...", total=100)
            with open(filename, "w") as f:
                f.write(content)
            progress.update(task, completed=100)

        self.show_panel(f"File '{filename}' created successfully!")

    def delete_file(self) -> None:
        """Delete a file."""
        filename = self.prompt("Enter filename to delete")
        
        if not os.path.exists(filename):
            self.show_panel(f"File '{filename}' does not exist!", title="Error")
            return

        if self.confirm(f"Are you sure you want to delete '{filename}'?"):
            with self.show_progress("Deleting file...", total=100) as progress:
                task = progress.add_task("Removing file...", total=100)
                os.remove(filename)
                progress.update(task, completed=100)

            self.show_panel(f"File '{filename}' deleted successfully!")

    def file_info(self) -> None:
        """Show information about a file."""
        filename = self.prompt("Enter filename")
        
        if not os.path.exists(filename):
            self.show_panel(f"File '{filename}' does not exist!", title="Error")
            return

        stat = os.stat(filename)
        info = f"""
        Name: {filename}
        Size: {stat.st_size:,} bytes
        Created: {stat.st_ctime}
        Modified: {stat.st_mtime}
        Accessed: {stat.st_atime}
        Is Directory: {os.path.isdir(filename)}
        Is File: {os.path.isfile(filename)}
        """

        self.show_panel(info, title="File Information")


# Example usage
if __name__ == "__main__":
    try:
        # Create and run the file manager
        file_manager = FileManager()
        file_manager.interactive_shell()
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")
        sys.exit(1) 