from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright, Page

class FetchContent(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def find_element(self, file_rein: str) -> str|None:
        pass

    @abstractmethod
    def close(self):
        pass


class PlaywrightFetchContent(FetchContent):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()

    def find_element(self, file_rein: str) -> str|None:
        url = self.base_url + file_rein
        try:
            self.page.goto(url)
            self.page.wait_for_load_state('domcontentloaded')
            return self._find_element_in_content(".ntee-category")
        except Exception as e:
            print(f"Error while trying to load the page: {url} - {e}")
            return None
    
    def _find_element_in_content(self, class_name: str):
        try:
            element = self.page.locator(class_name).first
            return element.text_content(timeout = 1000) if element else None
        except Exception as e:
            return None

    def close(self):
        self.page.close()
        self.browser.close()
        self.playwright.stop()


class SeleniumFetchContent(FetchContent):
    def __init__(self, base_url):
        super().__init__(base_url)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--enable-unsafe-swiftshader")  # Enable unsafe SwiftShader
        self.web_driver = webdriver.Chrome(options=chrome_options)

    def find_element(self, file_rein: str) -> str|None:
        self.url = self.base_url + file_rein
        self.web_driver.get(self.url)
        return self._find_element_by_class_name("ntee-category")
    
    def _find_element_by_class_name(self, class_name: str):
        try:
            element = self.web_driver.find_element(By.CLASS_NAME, class_name)
            return element.text
        except Exception as e:
            return None

    def close(self):
        self.web_driver.quit()