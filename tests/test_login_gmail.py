import time

import pytest

from PageObject.LoginPage import LoginPage

from TestData.LoginGmailData import LoginGmailData
from utilities.BaseClass import BaseClass


class TestLoginGmail(BaseClass):

    def test_login_gmail(self, get_data):
        log = self.getlogger()
        log.info("Created logger object from baseclass")
        log.info("Creating login page object, login_page")
        login_page = LoginPage(self.driver)
        log.info(self.driver.title)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "PLAYMASTER - CS:GO Training and Skills Practice"
        log.info(self.driver.current_url)
        log.info("Checking the present of early access sign-in button")
        self.verify_element_presence_using_cssSelector(login_page.early_access_signup_button_locator)
        lids_page = login_page.click_early_access_sign_button()
        log.info("Checking the present of google button")
        self.verify_element_presence_using_cssSelector(lids_page.gmail_button_locator)
        log.info("Clicking on the gmail button")
        time.sleep(3)
        log.info("Current URL of the page : "+self.driver.current_url)
        log.info("Current Title of the page : "+self.driver.title)
        gmail_login_page = lids_page.click_gmail_button()
        time.sleep(2)
        log.info("Current URL of the page : "+self.driver.current_url)
        log.info("Current Title of the page : "+self.driver.title)
        log.info("Enter the email address in the google page")
        gmail_login_page.enter_gmail_address(gmail=get_data["emailid"])
        log.info("Clicking the next button after entering the email address")
        gmail_login_page.click_next_button()
        time.sleep(3)
        log.info("Entering the gmail password")
        gmail_login_page.enter_gmail_password(password=get_data["password"])
        profile_page = gmail_login_page.click_final_next_button()
        log.info("Current URL of the page : "+self.driver.current_url)
        log.info("Current Title of the page : "+self.driver.title)
        time.sleep(13)
        log.info("Checking the presence of PlayMaster header after login")
        self.verify_element_presence_using_cssSelector(profile_page.profile_pm_header_locator)
        log.info("Current URL of the page : "+self.driver.current_url)
        log.info("Current Title of the page : "+self.driver.title)
        self.verify_element_presence_using_cssSelector(profile_page.profile_access_code_field_locator)
        log.info("Verified the presence of access code field")
        assert "access" in self.driver.current_url
        log.info("Verified the access code keyword in the current URL")
        self.verify_element_presence_using_cssSelector(profile_page.profile_access_code_continue_button_locator)
        log.info("Verified the presence of continue button")
        log.info("Login to PlayMaster through gmail was successful")
        # log.info("Checking the presence of profile name locator after login")
        # time.sleep(20)
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

    @pytest.fixture(params=LoginGmailData.test_login_gmail_data)
    def get_data(self, request):
        return request.param


