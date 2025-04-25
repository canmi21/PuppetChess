import sys
import time
from browser import Browser
from checker import Checker
from log import info, notice, action
from utils import is_chrome_running

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
    
    # Monitor for game URL with 30-second timeout
    info("Monitoring for lichess...")
    start_time = time.time()
    timeout = 30  # seconds
    while True:
        if time.time() - start_time > timeout:
            notice("No game URL found within 30 seconds, exiting")
            sys.exit(0)
        game_url = checker.check_for_game_url()
        if game_url:
            info(f"URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            time.sleep(2)
            # Check if it's the first move (your turn)
            if checker.check_first_move():
                info("It's your first move!")
            else:
                info("It's your opponent's move.")
            time.sleep(30)  # 30-second wait for debugging
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()