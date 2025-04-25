import re

class Checker:
    def __init__(self, browser):
        self.browser = browser
        self.game_url_pattern = re.compile(r'^https://lichess\.org/[A-Za-z0-9]{8}$')

    def check_for_game_url(self):
        """Check all open tabs for a lichess game URL"""
        tabs = self.browser.get_open_tabs()
        for url in tabs:
            if self.game_url_pattern.match(url):
                return url
        return None