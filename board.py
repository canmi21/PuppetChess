from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChessBoard:
    def __init__(self, driver):
        self.driver = driver

    def get_opponent_move(self):
        """Extract opponent's move from the chess board"""
        try:
            # Wait for the analysis board to load and be visible
            analysis_board = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="Analysis board"]'))
            )
            
            # Locate the move history container correctly
            parent_container = analysis_board.find_element(By.XPATH, './ancestor::div[contains(@class, "history-container")]')  # Adjusted for better accuracy
            moves_history = parent_container.find_elements(By.TAG_NAME, 'l4x')

            for move in moves_history:
                ply_number = move.find_element(By.TAG_NAME, 'i5z').text  # Get the round number
                move_text = move.find_elements(By.TAG_NAME, 'kwdb')  # Get the moves for this round
                
                if len(move_text) > 1:
                    # The opponent's move is the first one
                    opponent_move = move_text[0].text.strip()
                    return opponent_move

            return None
        except Exception as e:
            logging.error(f"Error extracting opponent's move: {str(e)}")
            return None

    def has_moves(self):
        """Check if the board has any moves recorded (if the move history exists)"""
        try:
            # Wait for the analysis board to be visible and accessible
            analysis_board = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@title="Analysis board"]'))
            )
            
            parent_container = analysis_board.find_element(By.XPATH, './ancestor::div[contains(@class, "history-container")]')  # Adjusted for better accuracy
            moves_history = parent_container.find_elements(By.TAG_NAME, 'l4x')
            return len(moves_history) > 0
        except Exception as e:
            logging.error(f"Error checking if moves exist: {str(e)}")
            return False