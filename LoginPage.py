from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from LoginPasswordPage import LoginPasswordPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.next_button_locator = '#login-signin'
        self.user_name_locator = '.phone-no'

    def enter_user_name(self, user_name):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.user_name_locator))).clear()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.user_name_locator))).send_keys(user_name)

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.next_button_locator))).click()
        return LoginPasswordPage(self.driver)
