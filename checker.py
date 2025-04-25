import re

def is_lichess_game_tab(url):
    pattern = r"^https://lichess.org/[A-Za-z0-9]{8}$"
    return bool(re.match(pattern, url))