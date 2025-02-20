from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

class FetchContent:
    def __init__(self, base_url):
        self.base_url = base_url
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        self.web_driver = webdriver.Chrome(options=chrome_options)

    def get_web_driver(self, file_rein: str) -> WebDriver:
        self.url = self.base_url + file_rein
        self.web_driver.get(self.url)
        return self.web_driver

    def close_web_driver(self):
        self.web_driver.quit()