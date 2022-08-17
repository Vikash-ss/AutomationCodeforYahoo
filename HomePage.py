from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from LoginPage import LoginPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.signin_link_locator = 'div.text'

    def click_signin(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.signin_link_locator))).click()
        return LoginPage(self.driver)