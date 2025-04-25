import sys
import time
from browser import Browser
from checker import Checker
from log import info, notice, action
from utils import is_chrome_running
from board import ChessBoard  # Import ChessBoard class
from counter import Counter  # Import Counter class

def main():
    # Check if there's any running chrome process
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
    counter = Counter()  # Initialize Counter for move counting

    # Monitor for game URL with 30-second timeout
    info("Monitoring for lichess...")
    start_time = time.time()
    timeout = 30  # seconds
    first_move = None  # Variable to track who goes first (True for you, False for opponent)

    while True:
        if time.time() - start_time > timeout:
            notice("No game URL found within 30 seconds, exiting")
            sys.exit(0)
        game_url = checker.check_for_game_url()
        if game_url:
            info(f"URL detected: {game_url}")
            action(f"Switching to game tab: {game_url}")
            browser.switch_to_tab(game_url)
            time.sleep(5)  # Wait for the tab to load

            chess_board = ChessBoard(browser.driver)
            if checker.check_first_move():
                info("It's your first move!")
                # Check if move history exists (if opponent already moved)
                if chess_board.has_moves():
                    info("Opponent has already made a move.")
                    first_move = False  # Opponent went first
                else:
                    info("No moves recorded yet, you go first!")
                    first_move = True
            else:
                info("It's your opponent's turn.")
                first_move = False

            # If opponent goes first, we need to read their move
            if not first_move:
                info("Waiting for opponent to make their move...")
                while not chess_board.has_moves():
                    time.sleep(1)  # Wait until opponent plays

                opponent_move = chess_board.get_opponent_move()
                if opponent_move:
                    info(f"Opponent's move: {opponent_move}")
                    counter.next_turn()  # Increment the turn count when opponent moves
                else:
                    info("Could not extract opponent's move.")

            time.sleep(600)  # Wait for debugging (adjust as needed)
            break
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()