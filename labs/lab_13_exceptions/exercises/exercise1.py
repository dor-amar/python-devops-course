"""Basic exception handling module."""

import os
import sys
import logging
import traceback
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union
from contextlib import contextmanager, ExitStack
from dataclasses import dataclass
from datetime import datetime
import structlog
from rich.console import Console
from rich.table import Table


# Configure logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger()


# Initialize Rich console
console = Console()


T = TypeVar('T')


@dataclass
class ErrorContext:
    """Context information for an error."""

    timestamp: datetime
    function_name: str
    line_number: int
    error_type: str
    error_message: str
    stack_trace: str
    context_data: Dict[str, Any]


class ExceptionHandler:
    """Handler for basic exception operations."""

    def __init__(self):
        """Initialize the exception handler."""
        self._error_contexts: List[ErrorContext] = []
        self._error_counts: Dict[str, int] = {}
        self._resource_cleanup: List[Callable] = []

    def handle_exception(
        self,
        func: Callable[..., T],
        *args: Any,
        **kwargs: Any
    ) -> Optional[T]:
        """Handle exceptions in a function call.

        Args:
            func: Function to call
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Optional[T]: Function result if successful
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self._log_exception(e, func.__name__)
            return None

    def handle_exception_with_retry(
        self,
        func: Callable[..., T],
        max_retries: int = 3,
        delay: float = 1.0,
        *args: Any,
        **kwargs: Any
    ) -> Optional[T]:
        """Handle exceptions with retry logic.

        Args:
            func: Function to call
            max_retries: Maximum number of retries
            delay: Delay between retries in seconds
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Optional[T]: Function result if successful
        """
        last_exception = None
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                self._log_exception(e, func.__name__, attempt + 1)
                if attempt < max_retries - 1:
                    import time
                    time.sleep(delay)
        return None

    def handle_exception_with_context(
        self,
        context_data: Dict[str, Any],
        func: Callable[..., T],
        *args: Any,
        **kwargs: Any
    ) -> Optional[T]:
        """Handle exceptions with additional context.

        Args:
            context_data: Additional context data
            func: Function to call
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Optional[T]: Function result if successful
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self._log_exception(e, func.__name__, context_data=context_data)
            return None

    @contextmanager
    def handle_resource(self, cleanup_func: Callable) -> None:
        """Handle resource cleanup with context manager.

        Args:
            cleanup_func: Function to call for cleanup
        """
        try:
            yield
        finally:
            cleanup_func()

    def register_cleanup(self, cleanup_func: Callable) -> None:
        """Register a cleanup function.

        Args:
            cleanup_func: Function to call for cleanup
        """
        self._resource_cleanup.append(cleanup_func)

    def cleanup_resources(self) -> None:
        """Run all registered cleanup functions."""
        for func in reversed(self._resource_cleanup):
            try:
                func()
            except Exception as e:
                self._log_exception(e, "cleanup_resources")

    def get_error_statistics(self) -> Dict[str, Any]:
        """Get error handling statistics.

        Returns:
            Dict[str, Any]: Error statistics
        """
        return {
            "total_errors": len(self._error_contexts),
            "error_counts": self._error_counts,
            "error_types": set(self._error_counts.keys()),
            "latest_error": self._error_contexts[-1] if self._error_contexts else None
        }

    def display_error_contexts(self) -> None:
        """Display error contexts in a formatted table."""
        if not self._error_contexts:
            console.print("[yellow]No error contexts recorded[/]")
            return

        table = Table(title="Error Contexts")
        table.add_column("Timestamp", style="cyan")
        table.add_column("Function", style="green")
        table.add_column("Error Type", style="red")
        table.add_column("Message", style="yellow")

        for context in self._error_contexts:
            table.add_row(
                context.timestamp.isoformat(),
                context.function_name,
                context.error_type,
                context.error_message
            )

        console.print(table)

    def _log_exception(
        self,
        exception: Exception,
        function_name: str,
        attempt: Optional[int] = None,
        context_data: Optional[Dict[str, Any]] = None
    ) -> None:
        """Log exception details.

        Args:
            exception: Exception that occurred
            function_name: Name of the function where exception occurred
            attempt: Attempt number for retries
            context_data: Additional context data
        """
        exc_type = type(exception).__name__
        exc_msg = str(exception)
        exc_trace = traceback.format_exc()

        # Update error counts
        self._error_counts[exc_type] = self._error_counts.get(exc_type, 0) + 1

        # Create error context
        context = ErrorContext(
            timestamp=datetime.utcnow(),
            function_name=function_name,
            line_number=sys.exc_info()[2].tb_lineno,
            error_type=exc_type,
            error_message=exc_msg,
            stack_trace=exc_trace,
            context_data=context_data or {}
        )
        self._error_contexts.append(context)

        # Log with structlog
        log_data = {
            "error_type": exc_type,
            "error_message": exc_msg,
            "function": function_name,
            "line_number": context.line_number,
            "attempt": attempt,
            "context": context_data
        }
        logger.error("exception_occurred", **log_data)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize exception handler
        handler = ExceptionHandler()

        # Example function that might raise an exception
        def divide(a: int, b: int) -> float:
            """Divide two numbers."""
            return a / b

        # Test basic exception handling
        print("Testing basic exception handling:")
        result = handler.handle_exception(divide, 10, 0)
        print(f"Result: {result}")

        # Test exception handling with retry
        print("\nTesting exception handling with retry:")
        def read_file(filename: str) -> str:
            """Read a file that might not exist."""
            with open(filename, 'r') as f:
                return f.read()

        result = handler.handle_exception_with_retry(
            read_file,
            max_retries=3,
            delay=1.0,
            filename="nonexistent.txt"
        )
        print(f"Result: {result}")

        # Test exception handling with context
        print("\nTesting exception handling with context:")
        context = {"user_id": 123, "operation": "data_processing"}
        result = handler.handle_exception_with_context(
            context,
            divide,
            20,
            0
        )
        print(f"Result: {result}")

        # Test resource cleanup
        print("\nTesting resource cleanup:")
        def cleanup():
            print("Cleaning up resources...")

        handler.register_cleanup(cleanup)
        with handler.handle_resource(cleanup):
            print("Using resources...")
            raise ValueError("Test error")

        # Display error statistics
        print("\nError statistics:")
        stats = handler.get_error_statistics()
        print(f"Total errors: {stats['total_errors']}")
        print(f"Error counts: {stats['error_counts']}")
        print(f"Error types: {stats['error_types']}")

        # Display error contexts
        print("\nError contexts:")
        handler.display_error_contexts()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        handler.cleanup_resources() 