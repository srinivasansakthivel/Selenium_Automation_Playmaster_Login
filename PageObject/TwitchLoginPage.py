import time

from selenium.webdriver.common.by import By

from PageObject.ProtonEmailPage import ProtonEmailPage


class TwitchLoginPage:
    twitch_username_field_locator = "input#login-username"
    twitch_username_field = (By.CSS_SELECTOR, "input#login-username")
    twitch_password_field = (By.CSS_SELECTOR, "input#password-input")
    twitch_login_button_locator = "//*[@id='root']/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button"
    twitch_login_button = (By.XPATH, "//*[@id='root']/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button")
    twitch_login_code_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/input[1]")

    def __init__(self, driver):
        self.driver = driver

    def enter_twitch_username(self, username):
        return self.driver.find_element(*TwitchLoginPage.twitch_username_field).send_keys(username)

    def enter_twitch_password(self, password):
        return self.driver.find_element(*TwitchLoginPage.twitch_password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*TwitchLoginPage.twitch_login_button).click()
        time.sleep(20)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get("https://protonmail.com/")
        proton_email_page = ProtonEmailPage(self.driver)
        return proton_email_page

    def enter_twitch_passcode(self, passcode):
        self.driver.find_element(*TwitchLoginPage.twitch_login_code_field).click()
        return self.driver.find_element(*TwitchLoginPage.twitch_login_code_field).send_keys(passcode)
