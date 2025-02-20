from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class FindElement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_element_by_class_name(self, class_name: str):
        try:
            element= self.driver.find_element(By.CLASS_NAME, class_name)
            return element.text
        except Exception as e:
            return None
       