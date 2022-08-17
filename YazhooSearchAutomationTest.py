from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from HomePage import HomePage

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('http://www.yahoo.com/')
homePage = HomePage(driver)
loginPage = homePage.click_signin()
loginPage.enter_user_name('vikashbruce@yahoo.com')
loginPasswordPage = loginPage.click_next_button()
loginPasswordPage.enter_password('Iambrucewayne')
searchOptionPage = loginPasswordPage.click_next_button()
searchOptionPage.enter_search_word('capgemini')
searchResultsPage = searchOptionPage.click_search_button()
searchResultsPage.print_result_url()
searchResultsPage.print_result_desc()
profileLinkPage = searchResultsPage.click_logo_button()
signOutPage = profileLinkPage.click_profile_button
signOutPage.click_account_button_locator()
signOutPage.click_signout_button()
driver.quit()
