import cv2
import numpy as np

class ChessBoard:
    def __init__(self):
        self.board_image = None

    def extract_scoreboard(self):
        """Extract the scoreboard area from the image using template matching"""
        capture_image = cv2.imread('capture.png')
        template = cv2.imread('res/analysis_board.png')
        gray_capture = cv2.cvtColor(capture_image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray_capture, gray_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8 
        loc = np.where(result >= threshold)

        if loc[0].size > 0:
            max_loc = (loc[1][0], loc[0][0])  # x, y
            w, h = template.shape[::-1]

            matched_region = capture_image[max_loc[1]:max_loc[1] + h, max_loc[0]:max_loc[0] + w]
            cv2.imwrite('match.png', matched_region)

            print("Match found! The scoreboard area has been extracted and saved as 'match.png'.")
            return matched_region
        else:
            print("No match found.")
            return None