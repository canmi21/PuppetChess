from selenium.webdriver.common.by import By

def is_opponent_first(browser):
    title = browser.driver.title.lower()
    if "your turn" in title:
        try:
            main_wrap = browser.driver.find_element(By.ID, "main-wrap")
            round_section = main_wrap.find_element(By.CLASS_NAME, "round")
            round_moves = round_section.find_elements(By.TAG_NAME, "rm6")
            if not round_moves:
                return True  # No moves yet, we go first
            return False  # Moves already made, opponent went first
        except Exception:
            return True  # Can't find elements, treat as first turn
    elif "waiting for" in title:
        return False  # Opponent to move first
    return False  # Default safe value


def get_opponent_move(browser, turn):
    try:
        main_wrap = browser.driver.find_element(By.ID, "main-wrap")
        round_section = main_wrap.find_element(By.CLASS_NAME, "round")
        rm6 = round_section.find_element(By.TAG_NAME, "rm6")
        l4x = rm6.find_element(By.TAG_NAME, "l4x")
        all_tags = l4x.find_elements(By.XPATH, "./*")

        move_index = (turn - 1) * 4 + 1  # Index of opponent's move
        if move_index < len(all_tags):
            return all_tags[move_index].text
    except Exception as e:
        return None
    return None