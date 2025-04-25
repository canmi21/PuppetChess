from manager import start_game, monitor_game
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    url = 'https://lichess.org/'
    options = Options()
    options.add_argument("--headless")
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    start_game(url)
    monitor_game(driver)

if __name__ == '__main__':
    main()
