from selenium.webdriver.common.by import By
from PageObject.LidsPage import LidsPage


class LoginPage:
    early_access_signup_button_locator = "button[type='button']"
    early_access_signup_button = (By.CSS_SELECTOR, "button[type='button']")

    def __init__(self, driver):
        self.driver = driver

    def click_early_access_sign_button(self):
        self.driver.find_element(*LoginPage.early_access_signup_button).click()
        lids_page = LidsPage(self.driver)
        return lids_page

