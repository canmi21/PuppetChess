import subprocess
import time
from browser import Browser
from checker import Checker
from utils import is_chrome_running
from log import info, notice, action

def main():
    # Check if Chrome is running
    if is_chrome_running():
        notice("Chrome is running, opening new tab to lichess.org")
        browser = Browser()
        browser.open_lichess_tab()
    else:
        notice("Chrome is not running, launching browser")
        browser = Browser()
        browser.launch_browser()
    
    # Initialize checker to monitor for game URL
    checker = Checker(browser)
    
    # Monitor for game URL
    info("Monitoring for lichess game URL...")
    while True:
        game_url = checker.check_for_game_url()
        if game_url:
            notice(f"Game URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()