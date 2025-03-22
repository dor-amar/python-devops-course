# Lab 21: Sending Notifications

This lab focuses on sending notifications through various channels (Slack, Telegram, and Email) in Python, including message formatting, error handling, and channel-specific features.

## Requirements

1. Create a module for Slack notifications with the following features:
   - Message sending to channels
   - Message formatting (blocks, attachments)
   - File uploads
   - Interactive components
   - Error handling

2. Create a module for Telegram notifications that includes:
   - Message sending to chats
   - Message formatting (markdown, HTML)
   - File and media sending
   - Inline keyboards
   - Bot commands

3. Create a module for email notifications that includes:
   - SMTP configuration
   - HTML and plain text emails
   - File attachments
   - Email templates
   - Error handling

## Directory Structure

```
labs/lab_21_notifications/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Slack notifications
    ├── exercise2.py  # Telegram notifications
    └── exercise3.py  # Email notifications
```

## Dependencies

- pytest
- rich
- slack-sdk
- python-telegram-bot
- python-dotenv
- jinja2 