import re

class Checker:
    def __init__(self, browser):
        self.browser = browser
        self.game_url_pattern = re.compile(r'^https://lichess\.org/[A-Za-z0-9]{6,15}$')

    def check_for_game_url(self):
        """Check all open tabs for a lichess game URL"""
        tabs = self.browser.get_open_tabs()
        for url in tabs:
            if self.game_url_pattern.match(url):
                return url
        return None

    def check_first_move(self):
        """Check if the game has started and if it's the player's turn"""
        tabs = self.browser.driver.window_handles  # Get window handles (tabs)
        for handle in tabs:
            self.browser.driver.switch_to.window(handle)
            title = self.browser.driver.title  # Get the title of the current tab
            if "your turn" in title.lower():
                return True