import requests
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

class FetchContent:
    def __init__(self, url):
        self.base_url = url

    def get_web_driver(self,file_rein: str) -> WebDriver:
        self.url = self.base_url + file_rein
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        web_driver = webdriver.Chrome(options=chrome_options)
        web_driver.get(self.url)
        return web_driver