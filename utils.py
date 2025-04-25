import subprocess

def is_chrome_running():
    """Check if google-chrome-stable process is running"""
    try:
        result = subprocess.run(
            ["pgrep", "-f", "google-chrome-stable"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False