"""System monitoring module."""

import os
import time
from typing import Any, Dict, List, Optional, Tuple, Union
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import psutil
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from apscheduler.schedulers.background import BackgroundScheduler
import json


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class SystemMonitor:
    """Manager for system monitoring."""

    def __init__(
        self,
        cpu_threshold: float = 80.0,
        memory_threshold: float = 80.0,
        disk_threshold: float = 80.0,
        network_threshold: float = 1000.0,  # MB/s
        check_interval: int = 60
    ):
        """Initialize the system monitor.

        Args:
            cpu_threshold: CPU usage threshold percentage
            memory_threshold: Memory usage threshold percentage
            disk_threshold: Disk usage threshold percentage
            network_threshold: Network traffic threshold in MB/s
            check_interval: Check interval in seconds
        """
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.disk_threshold = disk_threshold
        self.network_threshold = network_threshold
        self.check_interval = check_interval
        self.scheduler = BackgroundScheduler()
        self.metrics_history: List[Dict[str, Any]] = []
        self._setup_scheduler()

    def _setup_scheduler(self) -> None:
        """Set up the monitoring scheduler."""
        self.scheduler.add_job(
            self.check_system,
            'interval',
            seconds=self.check_interval
        )

    def start_monitoring(self) -> None:
        """Start the monitoring process."""
        console.print("\n[bold]Starting system monitoring...[/]")
        self.scheduler.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_monitoring()

    def stop_monitoring(self) -> None:
        """Stop the monitoring process."""
        console.print("\n[bold]Stopping system monitoring...[/]")
        self.scheduler.shutdown()

    def check_system(self) -> Dict[str, Any]:
        """Check system metrics.

        Returns:
            Dict[str, Any]: System metrics
        """
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'cpu': self._get_cpu_metrics(),
            'memory': self._get_memory_metrics(),
            'disk': self._get_disk_metrics(),
            'network': self._get_network_metrics(),
            'processes': self._get_process_metrics()
        }

        self.metrics_history.append(metrics)
        self._display_metrics(metrics)
        self._check_thresholds(metrics)

        return metrics

    def _get_cpu_metrics(self) -> Dict[str, float]:
        """Get CPU metrics.

        Returns:
            Dict[str, float]: CPU metrics
        """
        return {
            'percent': psutil.cpu_percent(interval=1),
            'count': psutil.cpu_count(),
            'frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 0
        }

    def _get_memory_metrics(self) -> Dict[str, float]:
        """Get memory metrics.

        Returns:
            Dict[str, float]: Memory metrics
        """
        memory = psutil.virtual_memory()
        return {
            'total': memory.total / (1024 ** 3),  # GB
            'available': memory.available / (1024 ** 3),  # GB
            'percent': memory.percent,
            'used': memory.used / (1024 ** 3)  # GB
        }

    def _get_disk_metrics(self) -> Dict[str, float]:
        """Get disk metrics.

        Returns:
            Dict[str, float]: Disk metrics
        """
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total / (1024 ** 3),  # GB
            'used': disk.used / (1024 ** 3),  # GB
            'free': disk.free / (1024 ** 3),  # GB
            'percent': disk.percent
        }

    def _get_network_metrics(self) -> Dict[str, float]:
        """Get network metrics.

        Returns:
            Dict[str, float]: Network metrics
        """
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent / (1024 ** 2),  # MB
            'bytes_recv': net_io.bytes_recv / (1024 ** 2),  # MB
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }

    def _get_process_metrics(self) -> List[Dict[str, Any]]:
        """Get process metrics.

        Returns:
            List[Dict[str, Any]]: Process metrics
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:10]

    def _check_thresholds(self, metrics: Dict[str, Any]) -> None:
        """Check if metrics exceed thresholds.

        Args:
            metrics: System metrics
        """
        alerts = []

        if metrics['cpu']['percent'] > self.cpu_threshold:
            alerts.append(f"CPU usage at {metrics['cpu']['percent']}%")

        if metrics['memory']['percent'] > self.memory_threshold:
            alerts.append(f"Memory usage at {metrics['memory']['percent']}%")

        if metrics['disk']['percent'] > self.disk_threshold:
            alerts.append(f"Disk usage at {metrics['disk']['percent']}%")

        if alerts:
            console.print("\n[bold red]Alerts:[/]")
            for alert in alerts:
                console.print(f"- {alert}")

    def _display_metrics(self, metrics: Dict[str, Any]) -> None:
        """Display system metrics in a formatted table.

        Args:
            metrics: System metrics
        """
        console.print(f"\n[bold]System Metrics - {metrics['timestamp']}[/]")

        # CPU Table
        cpu_table = Table(title="CPU Metrics")
        cpu_table.add_column("Metric", style="cyan")
        cpu_table.add_column("Value", style="green")
        for key, value in metrics['cpu'].items():
            cpu_table.add_row(key, str(value))
        console.print(cpu_table)

        # Memory Table
        memory_table = Table(title="Memory Metrics")
        memory_table.add_column("Metric", style="cyan")
        memory_table.add_column("Value", style="green")
        for key, value in metrics['memory'].items():
            memory_table.add_row(key, str(value))
        console.print(memory_table)

        # Disk Table
        disk_table = Table(title="Disk Metrics")
        disk_table.add_column("Metric", style="cyan")
        disk_table.add_column("Value", style="green")
        for key, value in metrics['disk'].items():
            disk_table.add_row(key, str(value))
        console.print(disk_table)

        # Network Table
        network_table = Table(title="Network Metrics")
        network_table.add_column("Metric", style="cyan")
        network_table.add_column("Value", style="green")
        for key, value in metrics['network'].items():
            network_table.add_row(key, str(value))
        console.print(network_table)

        # Top Processes Table
        process_table = Table(title="Top Processes")
        process_table.add_column("PID", style="cyan")
        process_table.add_column("Name", style="green")
        process_table.add_column("CPU %", style="yellow")
        process_table.add_column("Memory %", style="red")
        for proc in metrics['processes']:
            process_table.add_row(
                str(proc['pid']),
                proc['name'],
                f"{proc['cpu_percent']:.1f}%",
                f"{proc['memory_percent']:.1f}%"
            )
        console.print(process_table)

    def save_metrics(self, filename: Optional[str] = None) -> None:
        """Save metrics history to a file.

        Args:
            filename: Output filename (optional)
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"system_metrics_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(self.metrics_history, f, indent=2)
            console.print(f"[green]Saved metrics to {filename}[/]")

        except Exception as e:
            console.print(f"[red]Error saving metrics: {e}[/]")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize system monitor
        monitor = SystemMonitor(
            cpu_threshold=float(os.getenv('CPU_THRESHOLD', '80.0')),
            memory_threshold=float(os.getenv('MEMORY_THRESHOLD', '80.0')),
            disk_threshold=float(os.getenv('DISK_THRESHOLD', '80.0')),
            network_threshold=float(os.getenv('NETWORK_THRESHOLD', '1000.0')),
            check_interval=int(os.getenv('CHECK_INTERVAL', '60'))
        )

        # Start monitoring
        monitor.start_monitoring()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 