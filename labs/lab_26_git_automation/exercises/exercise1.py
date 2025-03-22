"""Basic Git operations module."""

import os
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import git
from git import Repo, GitCommandError
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class GitManager:
    """Manager for Git operations."""

    def __init__(
        self,
        repo_path: Union[str, Path],
        author_name: Optional[str] = None,
        author_email: Optional[str] = None
    ):
        """Initialize the Git manager.

        Args:
            repo_path: Path to the Git repository
            author_name: Git author name
            author_email: Git author email
        """
        self.repo_path = Path(repo_path)
        self.author_name = author_name or os.getenv('GIT_AUTHOR_NAME', 'Git Manager')
        self.author_email = author_email or os.getenv('GIT_AUTHOR_EMAIL', 'git@example.com')
        self.repo = self._initialize_repo()

    def _initialize_repo(self) -> Repo:
        """Initialize or open Git repository.

        Returns:
            Repo: Git repository object
        """
        try:
            if not self.repo_path.exists():
                console.print(f"[yellow]Initializing new repository at {self.repo_path}[/]")
                repo = git.Repo.init(self.repo_path)
            else:
                console.print(f"[green]Opening existing repository at {self.repo_path}[/]")
                repo = git.Repo(self.repo_path)

            # Configure Git user
            with repo.config_writer() as config:
                config.set_value('user', 'name', self.author_name)
                config.set_value('user', 'email', self.author_email)

            return repo

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            raise
        except Exception as e:
            console.print(f"[red]Error initializing repository: {e}[/]")
            raise

    def stage_files(self, files: Union[str, List[str], None] = None) -> List[str]:
        """Stage files for commit.

        Args:
            files: Files to stage (None for all changes)

        Returns:
            List[str]: List of staged files
        """
        try:
            if files is None:
                self.repo.git.add(all=True)
                staged = self.repo.index.diff('HEAD')
            else:
                if isinstance(files, str):
                    files = [files]
                self.repo.git.add(files)
                staged = [f for f in files if f in self.repo.index.diff('HEAD')]

            console.print(f"[green]Staged {len(staged)} files[/]")
            return staged

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return []

    def create_commit(
        self,
        message: str,
        files: Union[str, List[str], None] = None
    ) -> Optional[git.Commit]:
        """Create a commit.

        Args:
            message: Commit message
            files: Files to commit (None for all staged changes)

        Returns:
            Optional[git.Commit]: Created commit object
        """
        try:
            # Stage files if specified
            if files is not None:
                self.stage_files(files)

            # Check if there are changes to commit
            if not self.repo.index.diff('HEAD'):
                console.print("[yellow]No changes to commit[/]")
                return None

            # Create commit
            commit = self.repo.index.commit(
                message,
                author=git.Actor(self.author_name, self.author_email),
                committer=git.Actor(self.author_name, self.author_email)
            )

            console.print(f"[green]Created commit: {commit.hexsha[:8]}[/]")
            return commit

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return None

    def create_branch(self, name: str, start_point: str = 'HEAD') -> Optional[git.Head]:
        """Create a new branch.

        Args:
            name: Branch name
            start_point: Starting point (commit, branch, or tag)

        Returns:
            Optional[git.Head]: Created branch object
        """
        try:
            # Check if branch exists
            if name in self.repo.heads:
                console.print(f"[yellow]Branch {name} already exists[/]")
                return self.repo.heads[name]

            # Create branch
            branch = self.repo.create_head(name, start_point)
            console.print(f"[green]Created branch: {name}[/]")
            return branch

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return None

    def switch_branch(self, name: str) -> bool:
        """Switch to a branch.

        Args:
            name: Branch name

        Returns:
            bool: True if successful
        """
        try:
            # Check if branch exists
            if name not in self.repo.heads:
                console.print(f"[red]Branch {name} does not exist[/]")
                return False

            # Switch branch
            self.repo.heads[name].checkout()
            console.print(f"[green]Switched to branch: {name}[/]")
            return True

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return False

    def add_remote(
        self,
        name: str,
        url: str,
        fetch: bool = True
    ) -> Optional[git.Remote]:
        """Add a remote repository.

        Args:
            name: Remote name
            url: Remote URL
            fetch: Whether to fetch after adding

        Returns:
            Optional[git.Remote]: Created remote object
        """
        try:
            # Check if remote exists
            if name in self.repo.remotes:
                console.print(f"[yellow]Remote {name} already exists[/]")
                return self.repo.remotes[name]

            # Add remote
            remote = self.repo.create_remote(name, url)
            if fetch:
                remote.fetch()
            console.print(f"[green]Added remote: {name}[/]")
            return remote

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return None

    def push(
        self,
        remote_name: str = 'origin',
        branch_name: Optional[str] = None
    ) -> bool:
        """Push changes to remote.

        Args:
            remote_name: Remote name
            branch_name: Branch name (None for current branch)

        Returns:
            bool: True if successful
        """
        try:
            # Get remote
            if remote_name not in self.repo.remotes:
                console.print(f"[red]Remote {remote_name} does not exist[/]")
                return False

            remote = self.repo.remotes[remote_name]
            branch = branch_name or self.repo.active_branch.name

            # Push changes
            remote.push(branch)
            console.print(f"[green]Pushed to {remote_name}/{branch}[/]")
            return True

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return False

    def get_status(self) -> Dict[str, Any]:
        """Get repository status.

        Returns:
            Dict[str, Any]: Repository status
        """
        try:
            status = {
                'active_branch': self.repo.active_branch.name,
                'is_dirty': self.repo.is_dirty(),
                'untracked_files': self.repo.untracked_files,
                'modified_files': [item.a_path for item in self.repo.index.diff(None)],
                'staged_files': [item.a_path for item in self.repo.index.diff('HEAD')],
                'remotes': [remote.name for remote in self.repo.remotes],
                'branches': [branch.name for branch in self.repo.heads],
                'tags': [tag.name for tag in self.repo.tags],
                'last_commit': {
                    'hexsha': self.repo.head.commit.hexsha[:8],
                    'message': self.repo.head.commit.message,
                    'author': str(self.repo.head.commit.author),
                    'date': self.repo.head.commit.committed_datetime.isoformat()
                } if self.repo.head.is_valid() else None
            }

            self._display_status(status)
            return status

        except GitCommandError as e:
            console.print(f"[red]Git error: {e}[/]")
            return {}

    def _display_status(self, status: Dict[str, Any]) -> None:
        """Display repository status in a formatted table.

        Args:
            status: Repository status
        """
        console.print("\n[bold]Repository Status[/]")

        # Basic Info Table
        basic_table = Table(title="Basic Information")
        basic_table.add_column("Metric", style="cyan")
        basic_table.add_column("Value", style="green")
        basic_table.add_row("Active Branch", status['active_branch'])
        basic_table.add_row("Dirty", str(status['is_dirty']))
        console.print(basic_table)

        # Files Table
        files_table = Table(title="Files")
        files_table.add_column("Category", style="cyan")
        files_table.add_column("Count", style="green")
        files_table.add_column("Files", style="yellow")
        files_table.add_row(
            "Untracked",
            str(len(status['untracked_files'])),
            ", ".join(status['untracked_files']) or "None"
        )
        files_table.add_row(
            "Modified",
            str(len(status['modified_files'])),
            ", ".join(status['modified_files']) or "None"
        )
        files_table.add_row(
            "Staged",
            str(len(status['staged_files'])),
            ", ".join(status['staged_files']) or "None"
        )
        console.print(files_table)

        # Last Commit Table
        if status['last_commit']:
            commit_table = Table(title="Last Commit")
            commit_table.add_column("Field", style="cyan")
            commit_table.add_column("Value", style="green")
            for key, value in status['last_commit'].items():
                commit_table.add_row(key, str(value))
            console.print(commit_table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize Git manager
        git_manager = GitManager(
            repo_path=os.getenv('GIT_REPO_PATH', '.'),
            author_name=os.getenv('GIT_AUTHOR_NAME'),
            author_email=os.getenv('GIT_AUTHOR_EMAIL')
        )

        # Get repository status
        status = git_manager.get_status()

        # Create a new branch
        branch = git_manager.create_branch('feature/test')
        if branch:
            git_manager.switch_branch('feature/test')

        # Stage and commit changes
        staged = git_manager.stage_files()
        if staged:
            git_manager.create_commit("Test commit")

        # Add remote and push
        remote = git_manager.add_remote(
            'origin',
            os.getenv('GIT_REMOTE_URL', 'https://github.com/user/repo.git')
        )
        if remote:
            git_manager.push()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 