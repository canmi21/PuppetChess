import psutil
import time
from browser import Browser
from checker import Checker
from log import info, notice, action

def is_chrome_running():
    """Check if there's any running chrome process"""
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if 'chrome' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def main():
    # Check if there's any running chrome process
    if is_chrome_running():
        notice("Found chrome process, opening lichess tab")
        browser = Browser()
        browser.open_lichess_tab()
    else:
        notice("Chrome is not running, launching browser")
        browser = Browser()
        browser.launch_browser()
    
    # Initialize checker to monitor for game URL
    checker = Checker(browser)
    
    # Monitor for game URL
    info("Monitoring for lichess...")
    while True:
        game_url = checker.check_for_game_url()
        if game_url:
            notice(f"URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            time.sleep(10)
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()