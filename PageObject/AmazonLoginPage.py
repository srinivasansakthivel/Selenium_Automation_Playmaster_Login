import time

from selenium.webdriver.common.by import By

from PageObject.ProfilePage import ProfilePage


class AmazonLoginPage:
    amazon_email_field = (By.CSS_SELECTOR, "input#ap_email")
    amazon_password_field = (By.CSS_SELECTOR, "input#ap_password")
    amazon_sign_in_button_locator = "input#signInSubmit"
    amazon_sign_in_button = (By.CSS_SELECTOR, "input#signInSubmit")

    def __init__(self, driver):
        self.driver = driver

    def enter_amazon_email(self, email):
        return self.driver.find_element(*AmazonLoginPage.amazon_email_field).send_keys(email)

    def enter_amazon_password(self, password):
        return self.driver.find_element(*AmazonLoginPage.amazon_password_field).send_keys(password)

    def click_amazon_sign_in_button(self):
        self.driver.find_element(*AmazonLoginPage.amazon_sign_in_button).click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile_page = ProfilePage(self.driver)
        return profile_page
