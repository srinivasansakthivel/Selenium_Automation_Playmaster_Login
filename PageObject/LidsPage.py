import time
from selenium.webdriver.common.by import By
from PageObject.AmazonLoginPage import AmazonLoginPage
from PageObject.FacebookLoginPage import FacebookLoginPage
from PageObject.GmailLoginPage import GmailLoginPage
from PageObject.ProfilePage import ProfilePage
from PageObject.SpotifyLoginPage import SpotifyLoginPage
from PageObject.TwitchLoginPage import TwitchLoginPage


class LidsPage:
    email_field_locator = "#signin__email"
    email_field = (By.CSS_SELECTOR, email_field_locator)
    password_field = (By.CSS_SELECTOR, "#signin__password")
    login_button = (By.CSS_SELECTOR, "div.submit.centered:nth-child(9) > div.button")
    profile_name_locator = (By.CSS_SELECTOR, ".username___3ERcP")
    gmail_button_locator = "img#provider--slot_1_image"
    gmail_button = (By.CSS_SELECTOR, gmail_button_locator)
    facebook_button_locator = "img[id='provider--slot_2_image']"
    facebook_button = (By.CSS_SELECTOR, facebook_button_locator)
    scroll_right_arrow = (By.CSS_SELECTOR, "div#provider_scroll_right")
    spotify_button_locator = "img#provider--slot_6_image"
    spotify_button = (By.CSS_SELECTOR, spotify_button_locator)
    amazon_button_locator = "img#provider--slot_5_image"
    amazon_button = (By.CSS_SELECTOR, amazon_button_locator)
    twitch_button_locator = "img#provider--slot_3_image"
    twitch_button = (By.CSS_SELECTOR, twitch_button_locator)
    forgot_password_button_locator = "a#signin__forgot_password"
    forgot_password_button = (By.CSS_SELECTOR, forgot_password_button_locator)
    request_reset_button_locator = "#forgot__submit_container"
    request_reset_button = (By.CSS_SELECTOR, request_reset_button_locator)
    forgot_password_email_field = (By.CSS_SELECTOR, "input#forgot__email")
    forgot_password_status_area = "//div[contains(text(),'If the email below is valid, a password reset link will be " \
                                  "sent to your inbox.')] "
    reset_email_field = (By.CSS_SELECTOR, "input#reset__email")
    reset_email_password_field = (By.CSS_SELECTOR, "input#reset__password")
    update_password_button = (By.CSS_SELECTOR, "div#reset__submit_container")
    password_reset_successful_locator = "//div[@id='reset_success__header']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email):
        self.driver.find_element(*LidsPage.email_field).click()
        return self.driver.find_element(*LidsPage.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LidsPage.password_field).click()
        return self.driver.find_element(*LidsPage.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LidsPage.login_button).click()
        profile_page = ProfilePage(self.driver)
        return profile_page

    def click_gmail_button(self):
        self.driver.find_element(*LidsPage.gmail_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        gmail_login_page = GmailLoginPage(self.driver)
        return gmail_login_page

    def click_facebook_button(self):
        self.driver.find_element(*LidsPage.facebook_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        facebook_login_page = FacebookLoginPage(self.driver)
        return facebook_login_page

    def click_spotify_button(self):
        self.driver.find_element(*LidsPage.scroll_right_arrow).click()
        self.driver.find_element(*LidsPage.scroll_right_arrow).click()
        self.driver.find_element(*LidsPage.scroll_right_arrow).click()
        time.sleep(1)
        self.driver.find_element(*LidsPage.spotify_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        spotify_login_page = SpotifyLoginPage(self.driver)
        return spotify_login_page

    def click_amazon_button(self):
        self.driver.find_element(*LidsPage.scroll_right_arrow).click()
        self.driver.find_element(*LidsPage.scroll_right_arrow).click()
        time.sleep(1)
        self.driver.find_element(*LidsPage.amazon_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        amazon_login_page = AmazonLoginPage(self.driver)
        return amazon_login_page

    def click_twitch_button(self):
        self.driver.find_element(*LidsPage.twitch_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        twitch_login_page = TwitchLoginPage(self.driver)
        return twitch_login_page

    def click_forget_password_link(self):
        return self.driver.find_element(*LidsPage.forgot_password_button).click()

    def request_reset_password(self, email):
        self.driver.find_element(*LidsPage.forgot_password_email_field).send_keys(email)
        return self.driver.find_element(*LidsPage.request_reset_button).click()

    def update_email_password(self, new_password):
        # self.driver.find_element(*LidsPage.reset_email_field).clear()
        # self.driver.find_element(*LidsPage.reset_email_field).send_keys(email)
        self.driver.find_element(*LidsPage.reset_email_password_field).send_keys(new_password)
        return self.driver.find_element(*LidsPage.update_password_button).click()
