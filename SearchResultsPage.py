from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from ProfileLinkPage import ProfileLinkPage


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

        self.result_url_locator = 'span.d-ib.p-abs'
        self.result_desc_locator = '.fc-falcon'
        self.logo_button_locator = '#logo'

    def print_result_url(self):
        wait = WebDriverWait(self.driver, 15)
        print(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_url_locator))).text)

    def print_result_desc(self):
        wait = WebDriverWait(self.driver, 15)
        print(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_desc_locator))).text)

    def click_logo_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.logo_button_locator))).click()
        return ProfileLinkPage(self.driver)
