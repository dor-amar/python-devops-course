"""Slack notifications module."""

import os
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class SlackNotifier:
    """Manager for Slack notifications."""

    def __init__(self, token: Optional[str] = None):
        """Initialize the Slack notifier.

        Args:
            token: Slack bot token (optional, defaults to SLACK_BOT_TOKEN env var)
        """
        self.token = token or os.getenv('SLACK_BOT_TOKEN')
        if not self.token:
            raise ValueError("Slack bot token is required")
        self.client = WebClient(token=self.token)

    def send_message(
        self,
        channel: str,
        text: str,
        blocks: Optional[List[Dict[str, Any]]] = None,
        attachments: Optional[List[Dict[str, Any]]] = None,
        thread_ts: Optional[str] = None
    ) -> SlackResponse:
        """Send a message to a Slack channel.

        Args:
            channel: Channel ID or name
            text: Message text
            blocks: Message blocks (optional)
            attachments: Message attachments (optional)
            thread_ts: Thread timestamp for replies (optional)

        Returns:
            SlackResponse: Response from Slack API
        """
        try:
            message_kwargs = {
                'channel': channel,
                'text': text
            }

            if blocks:
                message_kwargs['blocks'] = blocks
            if attachments:
                message_kwargs['attachments'] = attachments
            if thread_ts:
                message_kwargs['thread_ts'] = thread_ts

            response = self.client.chat_postMessage(**message_kwargs)
            console.print(f"[green]Message sent to channel {channel}[/]")
            return response

        except SlackApiError as e:
            console.print(f"[red]Error sending message: {e.response['error']}[/]")
            raise

    def upload_file(
        self,
        channel: str,
        file_path: Union[str, Path],
        title: Optional[str] = None,
        initial_comment: Optional[str] = None,
        thread_ts: Optional[str] = None
    ) -> SlackResponse:
        """Upload a file to a Slack channel.

        Args:
            channel: Channel ID or name
            file_path: Path to file to upload
            title: File title (optional)
            initial_comment: Initial comment (optional)
            thread_ts: Thread timestamp for replies (optional)

        Returns:
            SlackResponse: Response from Slack API
        """
        try:
            upload_kwargs = {
                'channel': channel,
                'file': str(file_path)
            }

            if title:
                upload_kwargs['title'] = title
            if initial_comment:
                upload_kwargs['initial_comment'] = initial_comment
            if thread_ts:
                upload_kwargs['thread_ts'] = thread_ts

            response = self.client.files_upload(**upload_kwargs)
            console.print(f"[green]File uploaded to channel {channel}[/]")
            return response

        except SlackApiError as e:
            console.print(f"[red]Error uploading file: {e.response['error']}[/]")
            raise

    def create_block_message(
        self,
        title: str,
        text: str,
        color: str = "good"
    ) -> List[Dict[str, Any]]:
        """Create a message with blocks.

        Args:
            title: Message title
            text: Message text
            color: Color of the message (good, warning, danger)

        Returns:
            List[Dict[str, Any]]: List of blocks
        """
        return [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": title,
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"Status: {color}"
                    }
                ]
            }
        ]

    def create_attachment(
        self,
        title: str,
        text: str,
        color: str = "good",
        fields: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """Create a message attachment.

        Args:
            title: Attachment title
            text: Attachment text
            color: Color of the attachment (good, warning, danger)
            fields: List of fields to display

        Returns:
            Dict[str, Any]: Attachment dictionary
        """
        attachment = {
            "title": title,
            "text": text,
            "color": color,
            "mrkdwn_in": ["text", "fields"]
        }

        if fields:
            attachment["fields"] = fields

        return attachment

    def send_interactive_message(
        self,
        channel: str,
        title: str,
        text: str,
        buttons: List[Dict[str, Any]]
    ) -> SlackResponse:
        """Send an interactive message with buttons.

        Args:
            channel: Channel ID or name
            title: Message title
            text: Message text
            buttons: List of button configurations

        Returns:
            SlackResponse: Response from Slack API
        """
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{title}*\n{text}"
                }
            },
            {
                "type": "actions",
                "elements": buttons
            }
        ]

        return self.send_message(channel=channel, text=title, blocks=blocks)

    def display_message_info(self, response: SlackResponse) -> None:
        """Display message information in a formatted table.

        Args:
            response: Response from Slack API
        """
        table = Table(title="Message Information")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        for key, value in response.data.items():
            if isinstance(value, (str, int, bool)):
                table.add_row(key, str(value))

        console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize Slack notifier
        notifier = SlackNotifier()

        # Send a simple message
        console.print("\n[bold]Sending simple message...[/]")
        response = notifier.send_message(
            channel=os.getenv('SLACK_CHANNEL', '#general'),
            text="Hello from Python! 👋"
        )
        notifier.display_message_info(response)

        # Send a message with blocks
        console.print("\n[bold]Sending message with blocks...[/]")
        blocks = notifier.create_block_message(
            title="System Status",
            text="All systems operational",
            color="good"
        )
        response = notifier.send_message(
            channel=os.getenv('SLACK_CHANNEL', '#general'),
            text="System Status Update",
            blocks=blocks
        )
        notifier.display_message_info(response)

        # Send a message with attachments
        console.print("\n[bold]Sending message with attachments...[/]")
        fields = [
            {"title": "CPU Usage", "value": "45%", "short": True},
            {"title": "Memory Usage", "value": "60%", "short": True}
        ]
        attachment = notifier.create_attachment(
            title="System Metrics",
            text="Current system resource usage",
            color="warning",
            fields=fields
        )
        response = notifier.send_message(
            channel=os.getenv('SLACK_CHANNEL', '#general'),
            text="System Metrics Update",
            attachments=[attachment]
        )
        notifier.display_message_info(response)

        # Send an interactive message
        console.print("\n[bold]Sending interactive message...[/]")
        buttons = [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Approve",
                    "emoji": True
                },
                "style": "primary",
                "value": "approve"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Reject",
                    "emoji": True
                },
                "style": "danger",
                "value": "reject"
            }
        ]
        response = notifier.send_interactive_message(
            channel=os.getenv('SLACK_CHANNEL', '#general'),
            title="Action Required",
            text="Please review and take action on this request.",
            buttons=buttons
        )
        notifier.display_message_info(response)

        # Upload a file
        console.print("\n[bold]Uploading file...[/]")
        test_file = Path('test.txt')
        test_file.write_text('This is a test file.')
        response = notifier.upload_file(
            channel=os.getenv('SLACK_CHANNEL', '#general'),
            file_path=test_file,
            title="Test File",
            initial_comment="Here's a test file for you."
        )
        notifier.display_message_info(response)
        test_file.unlink()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 