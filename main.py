import sys
import time
from browser import Browser
from checker import Checker
from board import is_opponent_first, get_opponent_move
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

    # Monitor for game URL with timeout
    info("Monitoring for lichess...")
    start_time = time.time()
    timeout = 60
    while True:
        if time.time() - start_time > timeout:
            notice("No game URL found within 60 seconds, exiting")
            sys.exit(0)
        game_url = checker.check_for_game_url()
        if game_url:
            info(f"URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            break
        time.sleep(1)

    info("Waiting for game to start...")
    while True:
        title = browser.driver.title.lower()
        if "your turn" in title:
            break
        time.sleep(0.5)

    # Initialize game state
    turn = 1
    is_opponent_first = True

    if is_opponent_first(browser):
        info("Opponent moves first")
        time.sleep(6000)
    else:
        info("You move first")
        is_opponent_first = False
        time.sleep(6000)

if __name__ == "__main__":
    main()