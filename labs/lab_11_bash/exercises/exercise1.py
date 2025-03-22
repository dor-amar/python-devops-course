"""Shell command execution module."""

import os
import sys
import logging
import subprocess
from typing import Any, Dict, List, Optional, Tuple, Union
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
import psutil


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class CommandResult:
    """Result of a command execution."""

    returncode: int
    stdout: str
    stderr: str
    start_time: datetime
    end_time: datetime
    pid: Optional[int] = None


class ShellExecutor:
    """Executor for shell commands with advanced features."""

    def __init__(
        self,
        shell: bool = True,
        timeout: Optional[int] = None,
        env: Optional[Dict[str, str]] = None,
        cwd: Optional[Union[str, Path]] = None
    ):
        """Initialize the shell executor.

        Args:
            shell: Whether to run commands through the shell
            timeout: Command timeout in seconds
            env: Environment variables to use
            cwd: Working directory for commands
        """
        self.shell = shell
        self.timeout = timeout
        self.env = env or os.environ.copy()
        self.cwd = str(cwd) if cwd else None
        self._processes: Dict[int, subprocess.Popen] = {}

    def run(
        self,
        command: Union[str, List[str]],
        input_text: Optional[str] = None,
        capture_output: bool = True,
        check: bool = False
    ) -> CommandResult:
        """Run a command and return the result.

        Args:
            command: Command to run (string or list of arguments)
            input_text: Input to send to the command
            capture_output: Whether to capture stdout and stderr
            check: Whether to raise an exception on non-zero return code

        Returns:
            CommandResult: Command execution result

        Raises:
            subprocess.SubprocessError: If command execution fails
            subprocess.TimeoutExpired: If command times out
        """
        start_time = datetime.utcnow()
        try:
            logger.info(f"Running command: {command}")
            process = subprocess.Popen(
                command,
                shell=self.shell,
                timeout=self.timeout,
                env=self.env,
                cwd=self.cwd,
                input=input_text.encode() if input_text else None,
                capture_output=capture_output,
                text=True
            )
            self._processes[process.pid] = process

            stdout, stderr = process.communicate()
            end_time = datetime.utcnow()

            result = CommandResult(
                returncode=process.returncode,
                stdout=stdout,
                stderr=stderr,
                start_time=start_time,
                end_time=end_time,
                pid=process.pid
            )

            if check and result.returncode != 0:
                raise subprocess.CalledProcessError(
                    result.returncode,
                    command,
                    stdout,
                    stderr
                )

            return result

        except subprocess.SubprocessError as e:
            logger.error(f"Command failed: {e}")
            raise
        finally:
            if process.pid in self._processes:
                del self._processes[process.pid]

    def run_with_pipe(
        self,
        commands: List[Union[str, List[str]]]
    ) -> CommandResult:
        """Run multiple commands in a pipe.

        Args:
            commands: List of commands to pipe together

        Returns:
            CommandResult: Result of the last command

        Raises:
            subprocess.SubprocessError: If any command fails
        """
        if not commands:
            raise ValueError("No commands provided")

        start_time = datetime.utcnow()
        processes = []
        try:
            # Run first command
            first_cmd = commands[0]
            logger.info(f"Starting pipe with command: {first_cmd}")
            process = subprocess.Popen(
                first_cmd,
                shell=self.shell,
                env=self.env,
                cwd=self.cwd,
                stdout=subprocess.PIPE,
                text=True
            )
            processes.append(process)
            self._processes[process.pid] = process

            # Pipe remaining commands
            for cmd in commands[1:]:
                logger.info(f"Piping to command: {cmd}")
                process = subprocess.Popen(
                    cmd,
                    shell=self.shell,
                    env=self.env,
                    cwd=self.cwd,
                    stdin=processes[-1].stdout,
                    stdout=subprocess.PIPE,
                    text=True
                )
                processes.append(process)
                self._processes[process.pid] = process
                processes[-2].stdout.close()

            # Get output from last command
            stdout, stderr = processes[-1].communicate(timeout=self.timeout)
            returncode = processes[-1].returncode
            end_time = datetime.utcnow()

            return CommandResult(
                returncode=returncode,
                stdout=stdout,
                stderr=stderr,
                start_time=start_time,
                end_time=end_time,
                pid=processes[-1].pid
            )

        except subprocess.SubprocessError as e:
            logger.error(f"Pipe failed: {e}")
            raise
        finally:
            # Clean up processes
            for process in processes:
                try:
                    if process.pid in self._processes:
                        del self._processes[process.pid]
                    process.terminate()
                except ProcessLookupError:
                    pass

    def run_background(
        self,
        command: Union[str, List[str]],
        output_file: Optional[str] = None
    ) -> int:
        """Run a command in the background.

        Args:
            command: Command to run
            output_file: File to redirect output to

        Returns:
            int: Process ID
        """
        try:
            logger.info(f"Running background command: {command}")
            with open(output_file, 'w') if output_file else open(os.devnull, 'w') as f:
                process = subprocess.Popen(
                    command,
                    shell=self.shell,
                    env=self.env,
                    cwd=self.cwd,
                    stdout=f,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                self._processes[process.pid] = process
                return process.pid
        except Exception as e:
            logger.error(f"Failed to start background command: {e}")
            raise

    def kill_process(self, pid: int, force: bool = False) -> None:
        """Kill a running process.

        Args:
            pid: Process ID
            force: Whether to force kill the process
        """
        try:
            if pid in self._processes:
                process = self._processes[pid]
                if force:
                    process.kill()
                else:
                    process.terminate()
                del self._processes[pid]
                logger.info(f"Process {pid} terminated")
        except ProcessLookupError:
            logger.warning(f"Process {pid} not found")

    def get_process_info(self, pid: int) -> Dict[str, Any]:
        """Get information about a running process.

        Args:
            pid: Process ID

        Returns:
            Dict[str, Any]: Process information
        """
        try:
            process = psutil.Process(pid)
            return {
                "pid": process.pid,
                "name": process.name(),
                "status": process.status(),
                "cpu_percent": process.cpu_percent(),
                "memory_percent": process.memory_percent(),
                "create_time": datetime.fromtimestamp(process.create_time()),
                "cmdline": process.cmdline(),
                "username": process.username(),
                "num_threads": process.num_threads(),
                "num_fds": process.num_fds()
            }
        except psutil.NoSuchProcess:
            logger.warning(f"Process {pid} not found")
            return {}

    def cleanup(self) -> None:
        """Clean up all running processes."""
        for pid in list(self._processes.keys()):
            self.kill_process(pid, force=True)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize shell executor
        shell = ShellExecutor(shell=True)

        # Test basic command execution
        print("Testing basic command execution:")
        result = shell.run("echo 'Hello, World!'")
        print(f"Output: {result.stdout.strip()}")
        print(f"Return code: {result.returncode}")

        # Test command with input
        print("\nTesting command with input:")
        result = shell.run("grep 'World'", input_text="Hello\nHello, World!\nGoodbye")
        print(f"Output: {result.stdout.strip()}")

        # Test command pipe
        print("\nTesting command pipe:")
        result = shell.run_with_pipe([
            "echo 'Hello, World!'",
            "grep 'World'",
            "wc -w"
        ])
        print(f"Output: {result.stdout.strip()}")

        # Test background process
        print("\nTesting background process:")
        pid = shell.run_background(
            "sleep 10 && echo 'Background process completed'",
            output_file="background.log"
        )
        print(f"Started process with PID: {pid}")
        print("Process info:")
        print(shell.get_process_info(pid))

        # Clean up
        shell.cleanup()

    except Exception as e:
        print(f"Error: {e}") 