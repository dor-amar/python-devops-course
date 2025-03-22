"""Basic SSH operations module."""

import os
from typing import Any, Dict, List, Optional, Tuple, Union
from pathlib import Path
from dotenv import load_dotenv
import paramiko
from paramiko import SSHClient, SFTPClient
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class SSHManager:
    """Manager for SSH operations."""

    def __init__(
        self,
        hostname: str,
        username: str,
        password: Optional[str] = None,
        key_filename: Optional[str] = None,
        port: int = 22,
        timeout: float = 10.0
    ):
        """Initialize the SSH manager.

        Args:
            hostname: SSH server hostname
            username: SSH username
            password: SSH password (optional)
            key_filename: Path to private key file (optional)
            port: SSH port
            timeout: Connection timeout in seconds
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.port = port
        self.timeout = timeout
        self.client: Optional[SSHClient] = None
        self.sftp: Optional[SFTPClient] = None

    def connect(self) -> None:
        """Establish SSH connection."""
        try:
            self.client = SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            connect_kwargs = {
                'hostname': self.hostname,
                'username': self.username,
                'port': self.port,
                'timeout': self.timeout
            }

            if self.password:
                connect_kwargs['password'] = self.password
            if self.key_filename:
                connect_kwargs['key_filename'] = self.key_filename

            self.client.connect(**connect_kwargs)
            console.print(f"[green]Connected to {self.hostname}[/]")

        except Exception as e:
            console.print(f"[red]Connection error: {e}[/]")
            raise

    def disconnect(self) -> None:
        """Close SSH connection."""
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()
            console.print("[yellow]Disconnected from server[/]")

    def execute_command(
        self,
        command: str,
        timeout: Optional[float] = None
    ) -> Tuple[int, str, str]:
        """Execute a command on the remote server.

        Args:
            command: Command to execute
            timeout: Command timeout in seconds

        Returns:
            Tuple[int, str, str]: Exit code, stdout, stderr
        """
        if not self.client:
            raise RuntimeError("Not connected to server")

        try:
            stdin, stdout, stderr = self.client.exec_command(
                command,
                timeout=timeout
            )
            exit_code = stdout.channel.recv_exit_status()
            return exit_code, stdout.read().decode(), stderr.read().decode()

        except Exception as e:
            console.print(f"[red]Command execution error: {e}[/]")
            raise

    def execute_commands(
        self,
        commands: List[str],
        timeout: Optional[float] = None
    ) -> List[Tuple[str, int, str, str]]:
        """Execute multiple commands on the remote server.

        Args:
            commands: List of commands to execute
            timeout: Command timeout in seconds

        Returns:
            List[Tuple[str, int, str, str]]: List of (command, exit_code, stdout, stderr)
        """
        results = []
        for command in commands:
            exit_code, stdout, stderr = self.execute_command(command, timeout)
            results.append((command, exit_code, stdout, stderr))
        return results

    def open_sftp(self) -> SFTPClient:
        """Open SFTP session.

        Returns:
            SFTPClient: SFTP client
        """
        if not self.client:
            raise RuntimeError("Not connected to server")

        try:
            self.sftp = self.client.open_sftp()
            console.print("[green]SFTP session opened[/]")
            return self.sftp

        except Exception as e:
            console.print(f"[red]SFTP error: {e}[/]")
            raise

    def upload_file(
        self,
        local_path: Union[str, Path],
        remote_path: Union[str, Path]
    ) -> None:
        """Upload a file to the remote server.

        Args:
            local_path: Local file path
            remote_path: Remote file path
        """
        if not self.sftp:
            self.open_sftp()

        try:
            self.sftp.put(str(local_path), str(remote_path))
            console.print(f"[green]Uploaded {local_path} to {remote_path}[/]")

        except Exception as e:
            console.print(f"[red]Upload error: {e}[/]")
            raise

    def download_file(
        self,
        remote_path: Union[str, Path],
        local_path: Union[str, Path]
    ) -> None:
        """Download a file from the remote server.

        Args:
            remote_path: Remote file path
            local_path: Local file path
        """
        if not self.sftp:
            self.open_sftp()

        try:
            self.sftp.get(str(remote_path), str(local_path))
            console.print(f"[green]Downloaded {remote_path} to {local_path}[/]")

        except Exception as e:
            console.print(f"[red]Download error: {e}[/]")
            raise

    def list_directory(self, path: str = '.') -> List[str]:
        """List directory contents on the remote server.

        Args:
            path: Remote directory path

        Returns:
            List[str]: List of directory contents
        """
        if not self.sftp:
            self.open_sftp()

        try:
            return self.sftp.listdir(path)

        except Exception as e:
            console.print(f"[red]Directory listing error: {e}[/]")
            raise

    def display_command_results(
        self,
        results: List[Tuple[str, int, str, str]]
    ) -> None:
        """Display command execution results in a formatted table.

        Args:
            results: List of (command, exit_code, stdout, stderr) tuples
        """
        table = Table(title="Command Execution Results")
        table.add_column("Command", style="cyan")
        table.add_column("Exit Code", style="green")
        table.add_column("Output", style="yellow")
        table.add_column("Error", style="red")

        for command, exit_code, stdout, stderr in results:
            table.add_row(
                command,
                str(exit_code),
                stdout.strip() or "-",
                stderr.strip() or "-"
            )

        console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize SSH manager
        ssh = SSHManager(
            hostname=os.getenv('SSH_HOST', 'localhost'),
            username=os.getenv('SSH_USER', 'user'),
            password=os.getenv('SSH_PASSWORD'),
            key_filename=os.getenv('SSH_KEY_FILE')
        )

        # Connect to server
        ssh.connect()

        # Execute commands
        commands = [
            'pwd',
            'ls -la',
            'echo "Hello, World!"',
            'cat /etc/os-release'
        ]
        results = ssh.execute_commands(commands)
        ssh.display_command_results(results)

        # SFTP operations
        ssh.open_sftp()

        # List directory
        console.print("\n[bold]Remote directory contents:[/]")
        files = ssh.list_directory()
        for file in files:
            console.print(f"- {file}")

        # Upload file
        local_file = Path('test.txt')
        local_file.write_text('Hello, World!')
        ssh.upload_file(local_file, 'test.txt')

        # Download file
        ssh.download_file('test.txt', 'downloaded_test.txt')

        # Clean up
        local_file.unlink()
        Path('downloaded_test.txt').unlink()

        # Disconnect
        ssh.disconnect()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 