import psutil
import subprocess
import sys

def is_chrome_running():
    # Check if there's any running chrome process
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if 'chrome' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def open_chrome(url):
    # Try to open Chrome in a new tab if it's already running
    if is_chrome_running():
        subprocess.run(['google-chrome-stable', '--new-tab', url])
    else:
        # If Chrome isn't running, open a new Chrome window
        subprocess.run(['google-chrome-stable', '--new-window', url])

if __name__ == '__main__':
    url = 'https://lichess.org/'
    open_chrome(url)