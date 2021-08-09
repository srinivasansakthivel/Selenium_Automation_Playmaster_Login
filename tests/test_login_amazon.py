import time

import pytest

from PageObject.LoginPage import LoginPage
from PageObject.ProfilePage import ProfilePage
from TestData.LoginAmazonData import LoginAmazonData
from utilities.BaseClass import BaseClass


class TestLoginAmazon(BaseClass):

    def test_login_amazon(self, get_data):
        log = self.getlogger()
        log.info("Created logger object from baseclass")
        log.info("Creating login page object, login_page")
        login_page = LoginPage(self.driver)
        log.info("Title of the PlayMaster Page" + self.driver.title)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "PLAYMASTER - CS:GO Training and Skills Practice"
        log.info("Current Page URL :"+self.driver.current_url)
        log.info("Checking the present of early access sign-in button")
        self.verify_element_presence_using_cssSelector(login_page.early_access_signup_button_locator)
        lids_page = login_page.click_early_access_sign_button()
        time.sleep(3)
        amazon_login_page = lids_page.click_amazon_button()
        log.info("Clicked the amazon button in the Lids Page")
        log.info("Current Page URL :"+self.driver.current_url)
        self.verify_element_presence_using_cssSelector(amazon_login_page.amazon_sign_in_button_locator)
        amazon_login_page.enter_amazon_email(email=get_data["emailid"])
        log.info("Entered the email address in the Amazon login page")
        amazon_login_page.enter_amazon_password(password=get_data["password"])
        log.info("Entered the email password in the Amazon login page")
        profile_page = amazon_login_page.click_amazon_sign_in_button()
        log.info("Clicked the sign in button in the Amazon login page")
        log.info("Current URL of the page : " + self.driver.current_url)
        log.info("Current Title of the page : " + self.driver.title)
        time.sleep(13)
        log.info("Checking the presence of PlayMaster header after login")
        self.verify_element_presence_using_xpath(profile_page.profile_pm_header_locator)
        log.info("Current URL of the page : " + self.driver.current_url)
        log.info("Current Title of the page : " + self.driver.title)
        self.verify_element_presence_using_cssSelector(profile_page.profile_access_code_field_locator)
        log.info("Verified the presence of access code field")
        assert "access" in self.driver.current_url
        log.info("Verified the access code keyword in the current URL")
        self.verify_element_presence_using_cssSelector(profile_page.profile_access_code_continue_button_locator)
        log.info("Verified the presence of continue button")
        log.info("Login to PlayMaster through Amazon was successful")
        # log.info("Checking the presence of profile name locator after login")
        # time.sleep(13)
        # self.verify_element_presence_using_cssSelector(locator=ProfilePage.profile_name_field_locator)
        # player_profile_name = profile_page.get_profile_name()
        # log.info(f"Logged into {player_profile_name} account successfully")
        # log.info(self.driver.current_url)
        # player_profile_url = self.driver.current_url
        # profile_page.click_setting_button()
        # log.info("Clicked the setting button")
        # profile_page.click_account_settings_button()
        # log.info("Control in account settings page")
        # player_url_identifier = profile_page.get_url_identifier()
        # assert player_url_identifier in player_profile_url
        # profile_page.click_account_settings_close_button()
        # time.sleep(3)
        # log.info("Logged into PlayMaster successful through Amazon")

    @pytest.fixture(params=LoginAmazonData.test_login_amazon_data)
    def get_data(self, request):
        return request.param


