from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class Browser:
    def __init__(self):
        self.driver = None
        self.lichess_url = "https://lichess.org/"

    def launch_browser(self):
        """Launch Chrome and navigate to lichess.org"""
        chrome_options = Options()
        # Ensure Chrome runs in a way compatible with automation
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode
        chrome_options.add_argument("window-size=1920x1080")  # Set virtual screen size

        # Use webdriver-manager to handle ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(self.lichess_url)

    def open_lichess_tab(self):
        """Open a new tab with lichess.org if Chrome is already running"""
        if not self.driver:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            # .add_argument("--headless")  # Uncomment for headless mode
            chrome_options.add_argument("window-size=1920x1080")  # Set virtual screen size
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            self.driver.execute_script(f"window.open('{self.lichess_url}');")

    def switch_to_tab(self, url):
        """Switch to the tab with the specified URL"""
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            if self.driver.current_url == url:
                break

    def get_open_tabs(self):
        """Return a list of URLs of all open tabs"""
        tabs = []
        current_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            tabs.append(self.driver.current_url)
        self.driver.switch_to.window(current_window)
        return tabs

    def capture_screenshot(self, filename="capture.png"):
        """Capture a screenshot of the current page and save it"""
        screenshot = self.driver.get_screenshot_as_file(filename)
        return screenshot