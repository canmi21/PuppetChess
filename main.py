import sys
import time
from browser import Browser
from checker import Checker
from log import info, notice, action
from utils import is_chrome_running

def main():
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

    # Monitor for game URL with 60-second timeout
    info("Monitoring for lichess...")
    start_time = time.time()
    timeout = 60  # timeout for URL
    while True:
        if time.time() - start_time > timeout:
            notice("No game URL found within 60 seconds, exiting")
            sys.exit(0)
        game_url = checker.check_for_game_url()
        if game_url:
            info(f"URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            # Loop to wait for "Your turn"
            info("Waiting for the game to start...")
            time.sleep(0.5)
            while True:
                if "Your turn" in browser.driver.title:
                    info("It's your turn!")

                    time.sleep(60000)  # debug needed
                    sys.exit(0)
                time.sleep(1)
        time.sleep(1)

if __name__ == "__main__":
    main()