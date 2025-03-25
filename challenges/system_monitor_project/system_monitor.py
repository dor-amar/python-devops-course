"""
System Resource Monitor Project

Create a system monitoring tool that tracks CPU, memory, disk, and network usage.
This project will help you learn about:
- System metrics collection
- Data visualization
- Real-time monitoring
- Alert systems
- Configuration management

Requirements:
- psutil
- matplotlib
- yaml
"""

from typing import Dict, List, Optional
import time
import json
import yaml

class SystemMonitor:
    """System resource monitoring and alerting system."""
    
    def __init__(self, config_path: str = 'config.yaml'):
        """
        TODO: Initialize the monitoring system
        - Load configuration
        - Set up metrics storage
        - Initialize alert thresholds
        - Set up logging
        """
        pass

    def collect_metrics(self) -> Dict[str, float]:
        """
        TODO: Collect system metrics
        - CPU usage (per core and total)
        - Memory usage
        - Disk usage and I/O
        - Network statistics
        - Process information
        """
        pass

    def store_metrics(self, metrics: Dict[str, float]) -> None:
        """
        TODO: Store collected metrics
        - Save to file/database
        - Maintain history
        - Handle storage rotation
        """
        pass

    def check_alerts(self, metrics: Dict[str, float]) -> List[str]:
        """
        TODO: Check metrics against alert thresholds
        - Compare with configured thresholds
        - Generate alert messages
        - Handle alert cooldown
        - Support different alert levels
        """
        pass

    def generate_report(self, 
                       time_range: str = '1h') -> Dict[str, Any]:
        """
        TODO: Generate performance report
        - Calculate statistics
        - Create graphs
        - Format report data
        - Export in multiple formats
        """
        pass

    def start_monitoring(self, 
                        interval: int = 60) -> None:
        """
        TODO: Start the monitoring loop
        - Collect metrics periodically
        - Check for alerts
        - Generate reports
        - Handle interrupts
        """
        pass

class MetricsVisualizer:
    """
    TODO: Implement visualization for collected metrics
    - Real-time graphs
    - Historical trends
    - Resource usage patterns
    - Alert history
    """
    pass

def main():
    """
    TODO: Implement example usage
    - Load configuration
    - Start monitoring
    - Display metrics
    - Handle user commands
    """
    pass

if __name__ == "__main__":
    main() 