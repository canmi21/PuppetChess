from log import info, notice, action
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_opponent_first(browser):
    """Check if the opponent has made the first move."""
    try:
        WebDriverWait(browser.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "rm6"))
        )
        
        rounds = browser.driver.find_elements(By.TAG_NAME, "i5z")

        for round in rounds:
            if round.text == "1":
                return True
        return False

    except Exception as e:
        notice(f"Error checking opponent's first move: {e}")
        return False

from selenium.webdriver.common.by import By
import time

def get_opponent_move(browser, turn, side):
    xpath = f"//rm6/l4x/i5z[text()='{turn}']/following-sibling::kwdb"
    moves = browser.driver.find_elements(By.XPATH, xpath)
    
    if not moves:
        return None

    if side:
        return moves[0].text
    else:
        if len(moves) > 1:
            return moves[1].text
        else:
            return None