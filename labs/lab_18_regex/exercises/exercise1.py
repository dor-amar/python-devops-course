"""Basic regex operations module."""

import re
from typing import Any, Dict, List, Optional, Tuple, Union
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class RegexManager:
    """Manager for regular expression operations."""

    def __init__(self):
        """Initialize the regex manager."""
        self.compiled_patterns: Dict[str, re.Pattern] = {}

    def compile_pattern(self, pattern: str, flags: int = 0) -> re.Pattern:
        """Compile a regex pattern.

        Args:
            pattern: Regex pattern string
            flags: Regex flags

        Returns:
            re.Pattern: Compiled pattern
        """
        return re.compile(pattern, flags)

    def match(self, pattern: str, text: str, flags: int = 0) -> Optional[re.Match]:
        """Match a pattern at the beginning of text.

        Args:
            pattern: Regex pattern
            text: Text to match against
            flags: Regex flags

        Returns:
            Optional[re.Match]: Match object if found
        """
        return re.match(pattern, text, flags)

    def search(self, pattern: str, text: str, flags: int = 0) -> Optional[re.Match]:
        """Search for a pattern in text.

        Args:
            pattern: Regex pattern
            text: Text to search in
            flags: Regex flags

        Returns:
            Optional[re.Match]: Match object if found
        """
        return re.search(pattern, text, flags)

    def findall(self, pattern: str, text: str, flags: int = 0) -> List[str]:
        """Find all non-overlapping matches of pattern in text.

        Args:
            pattern: Regex pattern
            text: Text to search in
            flags: Regex flags

        Returns:
            List[str]: List of matches
        """
        return re.findall(pattern, text, flags)

    def finditer(self, pattern: str, text: str, flags: int = 0) -> re.MatchIterator:
        """Find all non-overlapping matches of pattern in text.

        Args:
            pattern: Regex pattern
            text: Text to search in
            flags: Regex flags

        Returns:
            re.MatchIterator: Iterator of match objects
        """
        return re.finditer(pattern, text, flags)

    def sub(self, pattern: str, repl: str, text: str, count: int = 0, flags: int = 0) -> str:
        """Replace pattern matches with replacement string.

        Args:
            pattern: Regex pattern
            repl: Replacement string
            text: Text to process
            count: Maximum number of replacements
            flags: Regex flags

        Returns:
            str: Processed text
        """
        return re.sub(pattern, repl, text, count, flags)

    def split(self, pattern: str, text: str, maxsplit: int = 0, flags: int = 0) -> List[str]:
        """Split text by pattern matches.

        Args:
            pattern: Regex pattern
            text: Text to split
            maxsplit: Maximum number of splits
            flags: Regex flags

        Returns:
            List[str]: List of split parts
        """
        return re.split(pattern, text, maxsplit, flags)

    def escape(self, text: str) -> str:
        """Escape special characters in text.

        Args:
            text: Text to escape

        Returns:
            str: Escaped text
        """
        return re.escape(text)

    def display_match(self, match: Optional[re.Match]) -> None:
        """Display match information in a formatted table.

        Args:
            match: Match object to display
        """
        if not match:
            console.print("[yellow]No match found[/]")
            return

        table = Table(title="Match Information")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Match", match.group(0))
        table.add_row("Start", str(match.start()))
        table.add_row("End", str(match.end()))
        table.add_row("Span", str(match.span()))

        if match.groups():
            table.add_row("Groups", str(match.groups()))
            for i, group in enumerate(match.groups(), 1):
                table.add_row(f"Group {i}", str(group))

        console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize regex manager
        regex = RegexManager()

        # Basic pattern matching
        console.print("\n[bold]Basic Pattern Matching[/]")
        text = "Hello, World!"
        pattern = r"Hello"
        match = regex.match(pattern, text)
        regex.display_match(match)

        # Character classes
        console.print("\n[bold]Character Classes[/]")
        text = "The quick brown fox jumps over the lazy dog"
        pattern = r"[aeiou]"
        matches = regex.findall(pattern, text)
        console.print(f"Vowels found: {matches}")

        # Quantifiers
        console.print("\n[bold]Quantifiers[/]")
        text = "aaabbbccc"
        pattern = r"a+"
        match = regex.search(pattern, text)
        regex.display_match(match)

        # Grouping
        console.print("\n[bold]Grouping[/]")
        text = "John Doe (30) - john@example.com"
        pattern = r"(\w+)\s+(\w+)\s+\((\d+)\)"
        match = regex.search(pattern, text)
        regex.display_match(match)

        # Substitution
        console.print("\n[bold]Substitution[/]")
        text = "The cat and the cat"
        pattern = r"cat"
        repl = "dog"
        result = regex.sub(pattern, repl, text)
        console.print(f"Original: {text}")
        console.print(f"Modified: {result}")

        # Splitting
        console.print("\n[bold]Splitting[/]")
        text = "one,two,three"
        pattern = r","
        parts = regex.split(pattern, text)
        console.print(f"Split parts: {parts}")

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 