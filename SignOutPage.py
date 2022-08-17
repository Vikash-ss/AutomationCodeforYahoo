from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class SignOutPage:

    def __init__(self, driver):
        self.driver = driver

        self.account_menu_locator = "//label[@id='ybarAccountMenuOpener']/div/img"
        self.signout_button_locator = '#profile-signout-link'

    def click_account_button_locator(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.account_menu_locator))).click()

    def click_signout_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.signout_button_locator))).click()

