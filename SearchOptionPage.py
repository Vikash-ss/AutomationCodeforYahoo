from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from SearchResultsPage import SearchResultsPage


class SearchOptionPage:

    def __init__(self, driver):
        self.driver = driver

        self.search_combobox_locator = 'p'
        self.search_box_button_locator = 'button[type="submit"]'

    def enter_search_word(self, search_word):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.NAME, self.search_combobox_locator))).clear()
        wait.until(EC.visibility_of_element_located((By.NAME, self.search_combobox_locator))).send_keys(search_word)

    def click_search_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_box_button_locator))).click()
        return SearchResultsPage(self.driver)

