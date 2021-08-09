import time

from selenium.webdriver.common.by import By

from PageObject.ProfilePage import ProfilePage


class SpotifyLoginPage:

    spotify_username_field = (By.CSS_SELECTOR, "input#login-username")
    spotify_password_field = (By.CSS_SELECTOR, "input#login-password")
    spotify_login_button = (By.CSS_SELECTOR, "button#login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_spotify_email(self, email):
        return self.driver.find_element(*SpotifyLoginPage.spotify_username_field).send_keys(email)

    def enter_spotify_password(self, password):
        return self.driver.find_element(*SpotifyLoginPage.spotify_password_field).send_keys(password)

    def click_spotify_login_button(self):
        self.driver.find_element(*SpotifyLoginPage.spotify_login_button).click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile_page = ProfilePage(self.driver)
        return profile_page







