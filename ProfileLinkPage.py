from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SignOutPage import SignOutPage


class ProfileLinkPage:

    def __init__(self, driver):
        self.driver = driver

        self.profile_button_locator = '#ysignout'

    @property
    def click_profile_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.profile_button_locator))).click()
        return SignOutPage(self.driver)
