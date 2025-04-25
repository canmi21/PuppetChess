from checker import is_lichess_game_tab
from browser import open_chrome, switch_to_tab
import time

def start_game(url):
    open_chrome(url)
    print(f"Game started at {url}")

def monitor_game(driver):
    while True:
        if check_and_switch_tab(driver, is_lichess_game_tab):
            print("Game started, switching to game tab")
            break
        time.sleep(2)

def check_and_switch_tab(driver, is_target_tab_func):
    tabs = driver.window_handles
    for tab in tabs:
        driver.switch_to.window(tab)
        url = driver.current_url
        if is_target_tab_func(url):
            return True
    return False
