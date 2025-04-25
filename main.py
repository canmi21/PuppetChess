import sys
import time
from browser import Browser
from checker import Checker
from log import info, notice, action
from utils import is_chrome_running
from board import ChessBoard  # Import ChessBoard class
from counter import Counter  # Import Counter class

def main():
    # Check if there's any running chrome process
    if is_chrome_running():
        info("Found chrome process, opening lichess tab")
        browser = Browser()
        browser.open_lichess_tab()
    else:
        info("Chrome is not running, launching browser")
        browser = Browser()
        browser.launch_browser()
    
    # Initialize checker to monitor for game URL
    checker = Checker(browser)
    counter = Counter()  # Initialize Counter for move counting

    # Monitor for game URL with 30-second timeout
    info("Monitoring for lichess...")

if __name__ == "__main__":
    main()