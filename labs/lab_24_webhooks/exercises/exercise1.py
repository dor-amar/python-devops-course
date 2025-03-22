"""Basic webhook functionality module."""

import os
import json
from typing import Any, Dict, Optional, Union
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class WebhookServer:
    """Server for handling webhook requests."""

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 5000,
        debug: bool = False
    ):
        """Initialize the webhook server.

        Args:
            host: Server host
            port: Server port
            debug: Enable debug mode
        """
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.debug = debug
        self._setup_routes()

    def _setup_routes(self) -> None:
        """Set up webhook routes."""
        self.app.add_url_rule(
            "/webhook",
            "webhook",
            self.handle_webhook,
            methods=["POST"]
        )

    def handle_webhook(self) -> Response:
        """Handle incoming webhook requests.

        Returns:
            Response: Flask response
        """
        try:
            # Log request details
            self._log_request()

            # Validate request
            if not self._validate_request():
                return jsonify({
                    "error": "Invalid request",
                    "status": "error"
                }), 400

            # Get request data
            data = self._get_request_data()
            if not data:
                return jsonify({
                    "error": "No data provided",
                    "status": "error"
                }), 400

            # Process webhook
            result = self._process_webhook(data)

            # Return success response
            return jsonify({
                "message": "Webhook processed successfully",
                "status": "success",
                "data": result
            }), 200

        except Exception as e:
            console.print(f"[red]Error processing webhook: {e}[/]")
            return jsonify({
                "error": str(e),
                "status": "error"
            }), 500

    def _validate_request(self) -> bool:
        """Validate the incoming request.

        Returns:
            bool: True if request is valid
        """
        # Check content type
        if not request.is_json:
            console.print("[yellow]Invalid content type[/]")
            return False

        # Check request method
        if request.method != "POST":
            console.print("[yellow]Invalid request method[/]")
            return False

        return True

    def _get_request_data(self) -> Optional[Dict[str, Any]]:
        """Get and parse request data.

        Returns:
            Optional[Dict[str, Any]]: Parsed request data
        """
        try:
            return request.get_json()
        except Exception as e:
            console.print(f"[red]Error parsing request data: {e}[/]")
            return None

    def _process_webhook(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process webhook data.

        Args:
            data: Webhook data

        Returns:
            Dict[str, Any]: Processing result
        """
        # Add timestamp
        data["processed_at"] = datetime.utcnow().isoformat()

        # Log processing
        console.print("[green]Processing webhook data:[/]")
        self._display_data(data)

        return data

    def _log_request(self) -> None:
        """Log request details."""
        console.print("\n[bold]Incoming Webhook Request[/]")
        console.print(f"Method: {request.method}")
        console.print(f"URL: {request.url}")
        console.print(f"Headers: {dict(request.headers)}")
        console.print(f"Remote Address: {request.remote_addr}")

    def _display_data(self, data: Dict[str, Any]) -> None:
        """Display data in a formatted table.

        Args:
            data: Data to display
        """
        table = Table(title="Webhook Data")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="green")

        for key, value in data.items():
            if isinstance(value, (str, int, float, bool)):
                table.add_row(key, str(value))
            else:
                table.add_row(key, json.dumps(value))

        console.print(table)

    def save_webhook_data(
        self,
        data: Dict[str, Any],
        filename: Optional[str] = None
    ) -> None:
        """Save webhook data to a file.

        Args:
            data: Webhook data
            filename: Output filename (optional)
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"webhook_data_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            console.print(f"[green]Saved webhook data to {filename}[/]")

        except Exception as e:
            console.print(f"[red]Error saving webhook data: {e}[/]")

    def run(self) -> None:
        """Run the webhook server."""
        console.print(f"\n[bold]Starting webhook server on {self.host}:{self.port}[/]")
        self.app.run(
            host=self.host,
            port=self.port,
            debug=self.debug
        )


# Example usage
if __name__ == "__main__":
    try:
        # Initialize webhook server
        server = WebhookServer(
            host=os.getenv('WEBHOOK_HOST', '0.0.0.0'),
            port=int(os.getenv('WEBHOOK_PORT', '5000')),
            debug=os.getenv('WEBHOOK_DEBUG', 'False').lower() == 'true'
        )

        # Run server
        server.run()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 