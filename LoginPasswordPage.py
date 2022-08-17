from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# from UserHomePage import UserHomePage
from SearchOptionPage import SearchOptionPage


class LoginPasswordPage:

    def __init__(self, driver):
        self.driver = driver

        self.next_button_locator = '#login-signin'
        self.password_text_box_locator = '#login-passwd'

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.password_text_box_locator))).clear()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.password_text_box_locator))).send_keys(password)

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.next_button_locator))).click()
        return SearchOptionPage(self.driver)