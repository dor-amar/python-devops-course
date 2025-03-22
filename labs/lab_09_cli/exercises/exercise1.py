"""Subprocess management module for running shell commands."""

import os
import subprocess
import logging
from typing import Dict, List, Optional, Tuple, Union
from pathlib import Path


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class CommandRunner:
    """Class for running and managing shell commands."""

    def __init__(
        self,
        shell: bool = False,
        timeout: Optional[int] = None,
        env: Optional[Dict[str, str]] = None,
        cwd: Optional[Union[str, Path]] = None
    ):
        """Initialize the command runner.

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

    def run(
        self,
        command: Union[str, List[str]],
        input_text: Optional[str] = None,
        capture_output: bool = True
    ) -> subprocess.CompletedProcess:
        """Run a command and return the result.

        Args:
            command: Command to run (string or list of arguments)
            input_text: Input to send to the command
            capture_output: Whether to capture stdout and stderr

        Returns:
            subprocess.CompletedProcess: Command result

        Raises:
            subprocess.SubprocessError: If command execution fails
            subprocess.TimeoutExpired: If command times out
        """
        try:
            logger.info(f"Running command: {command}")
            result = subprocess.run(
                command,
                shell=self.shell,
                timeout=self.timeout,
                env=self.env,
                cwd=self.cwd,
                input=input_text.encode() if input_text else None,
                capture_output=capture_output,
                text=True
            )
            logger.debug(f"Command completed with return code: {result.returncode}")
            return result
        except subprocess.SubprocessError as e:
            logger.error(f"Command failed: {e}")
            raise

    def run_with_output(
        self,
        command: Union[str, List[str]],
        input_text: Optional[str] = None
    ) -> Tuple[str, str, int]:
        """Run a command and return stdout, stderr, and return code.

        Args:
            command: Command to run
            input_text: Input to send to the command

        Returns:
            Tuple[str, str, int]: (stdout, stderr, return_code)
        """
        result = self.run(command, input_text=input_text)
        return result.stdout, result.stderr, result.returncode

    def run_successful(
        self,
        command: Union[str, List[str]],
        input_text: Optional[str] = None
    ) -> bool:
        """Run a command and return whether it was successful.

        Args:
            command: Command to run
            input_text: Input to send to the command

        Returns:
            bool: True if command succeeded, False otherwise
        """
        try:
            result = self.run(command, input_text=input_text)
            return result.returncode == 0
        except subprocess.SubprocessError:
            return False

    def run_with_pipe(
        self,
        commands: List[Union[str, List[str]]]
    ) -> subprocess.CompletedProcess:
        """Run multiple commands in a pipe.

        Args:
            commands: List of commands to pipe together

        Returns:
            subprocess.CompletedProcess: Result of the last command

        Raises:
            subprocess.SubprocessError: If any command fails
        """
        if not commands:
            raise ValueError("No commands provided")

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
                processes[-2].stdout.close()

            # Get output from last command
            stdout, stderr = processes[-1].communicate(timeout=self.timeout)
            returncode = processes[-1].returncode

            logger.debug(f"Pipe completed with return code: {returncode}")
            return subprocess.CompletedProcess(
                args=commands[-1],
                returncode=returncode,
                stdout=stdout,
                stderr=stderr
            )

        except subprocess.SubprocessError as e:
            logger.error(f"Pipe failed: {e}")
            raise
        finally:
            # Clean up processes
            for process in processes:
                try:
                    process.terminate()
                except ProcessLookupError:
                    pass

    def set_env(self, key: str, value: str) -> None:
        """Set an environment variable.

        Args:
            key: Environment variable name
            value: Environment variable value
        """
        self.env[key] = value

    def get_env(self, key: str) -> Optional[str]:
        """Get an environment variable value.

        Args:
            key: Environment variable name

        Returns:
            Optional[str]: Environment variable value
        """
        return self.env.get(key)

    def unset_env(self, key: str) -> None:
        """Remove an environment variable.

        Args:
            key: Environment variable name
        """
        self.env.pop(key, None)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize command runner
        runner = CommandRunner(shell=True)

        # Test basic command execution
        print("Testing basic command execution:")
        result = runner.run("echo 'Hello, World!'")
        print(f"Output: {result.stdout.strip()}")

        # Test command with input
        print("\nTesting command with input:")
        result = runner.run("grep 'World'", input_text="Hello\nHello, World!\nGoodbye")
        print(f"Output: {result.stdout.strip()}")

        # Test command pipe
        print("\nTesting command pipe:")
        result = runner.run_with_pipe([
            "echo 'Hello, World!'",
            "grep 'World'",
            "wc -w"
        ])
        print(f"Output: {result.stdout.strip()}")

        # Test environment variables
        print("\nTesting environment variables:")
        runner.set_env("TEST_VAR", "test_value")
        result = runner.run("echo $TEST_VAR")
        print(f"Output: {result.stdout.strip()}")

        # Test working directory
        print("\nTesting working directory:")
        runner = CommandRunner(shell=True, cwd="/tmp")
        result = runner.run("pwd")
        print(f"Output: {result.stdout.strip()}")

    except Exception as e:
        print(f"Error: {e}") 