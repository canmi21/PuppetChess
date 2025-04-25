from datetime import datetime

def info(message):
    """Print an info log message with timestamp and '-' prefix."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp} - {message}")

def notice(message):
    """Print a notice log message with timestamp and '!' prefix."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp} ! {message}")

def action(message):
    """Print an action log message with timestamp and '>' prefix."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp} > {message}")