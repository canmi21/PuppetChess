import psutil
import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def is_chrome_running():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if 'chrome' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def open_chrome(url):
    if is_chrome_running():
        subprocess.run(['google-chrome-stable', '--new-tab', url])
    else:
        subprocess.run(['google-chrome-stable', '--new-window', url])

def switch_to_tab(driver, url):
    driver.get(url)
