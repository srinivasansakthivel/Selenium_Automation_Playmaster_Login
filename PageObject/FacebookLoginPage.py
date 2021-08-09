import time

from selenium.webdriver.common.by import By

from PageObject.ProfilePage import ProfilePage


class FacebookLoginPage:
    facebook_email_field = (By.CSS_SELECTOR, "input#email")
    facebook_password_field = (By.CSS_SELECTOR, "input#pass")
    facebook_login_button_locator = "label#loginbutton"
    facebook_login_button = (By.CSS_SELECTOR, "label#loginbutton")

    def __init__(self, driver):
        self.driver = driver

    def enter_facebook_email(self, email):
        return self.driver.find_element(*FacebookLoginPage.facebook_email_field).send_keys(email)

    def enter_facebook_password(self, password):
        return self.driver.find_element(*FacebookLoginPage.facebook_password_field).send_keys(password)

    def click_facebook_login_button(self):
        self.driver.find_element(*FacebookLoginPage.facebook_login_button).click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile_page = ProfilePage(self.driver)
        return profile_page
