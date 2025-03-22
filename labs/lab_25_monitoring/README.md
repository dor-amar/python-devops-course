# Lab 25: Custom Monitoring Scripts with Alerts

This lab focuses on creating custom monitoring scripts that send alerts, including system monitoring, resource tracking, alert generation, and notification delivery through various channels.

## Requirements

1. Create a module for system monitoring with the following features:
   - CPU usage monitoring
   - Memory usage tracking
   - Disk space monitoring
   - Network traffic analysis
   - Process monitoring

2. Create a module for alert management that includes:
   - Alert thresholds
   - Alert severity levels
   - Alert history
   - Alert suppression
   - Alert aggregation

3. Create a module for notification delivery that includes:
   - Email notifications
   - Slack notifications
   - SMS alerts
   - Custom webhook integration
   - Alert templates

## Directory Structure

```
labs/lab_25_monitoring/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # System monitoring
    ├── exercise2.py  # Alert management
    └── exercise3.py  # Notification delivery
```

## Dependencies

- pytest
- rich
- psutil
- requests
- python-dotenv
- jinja2
- apscheduler
- slack-sdk
- twilio
- smtplib3 