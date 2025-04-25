from selenium.webdriver.common.by import By
import logging

class ChessBoard:
    def __init__(self, driver):
        self.driver = driver

    def get_opponent_move(self):
        """Extract opponent's move from the chess board"""
        try:
            # Find the container that holds the chess moves (identified by 'title="Analysis board"')
            analysis_board = self.driver.find_element(By.XPATH, '//*[@title="Analysis board"]')
            parent_container = analysis_board.find_element(By.XPATH, './ancestor::rm6')  # Find the parent 'rm6' element containing moves

            # Find the move history inside the container (the <l4x> elements)
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
            analysis_board = self.driver.find_element(By.XPATH, '//*[@title="Analysis board"]')
            parent_container = analysis_board.find_element(By.XPATH, './ancestor::rm6')
            moves_history = parent_container.find_elements(By.TAG_NAME, 'l4x')
            return len(moves_history) > 0
        except Exception as e:
            logging.error(f"Error checking if moves exist: {str(e)}")
            return False