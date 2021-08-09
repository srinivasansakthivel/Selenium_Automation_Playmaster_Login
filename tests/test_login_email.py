import time
import pytest
from PageObject.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from PageObject.ProfilePage import ProfilePage
from TestData.LoginEmailData import LoginEmailData


class TestLoginEmail(BaseClass):

    def test_login_email(self, get_data):
        log = self.getlogger()
        log.info("Created logger object from baseclass")
        log.info("Creating login page object")
        login_page = LoginPage(self.driver)
        log.info("Current Page Title : "+self.driver.title)
        assert self.driver.title == "PLAYMASTER - CS:GO Training and Skills Practice"
        log.info("Current Page URL :"+self.driver.current_url)
        log.info("Checking the present of early access sign-in button")
        self.verify_element_presence_using_cssSelector(login_page.early_access_signup_button_locator)
        lids_page = login_page.click_early_access_sign_button()
        log.info("Clicked on early access sign-in button and navigated to the LIDS login page")
        log.info("Current Page URL :"+self.driver.current_url)
        time.sleep(2)
        log.info("Entering the email address")
        self.verify_element_presence_using_cssSelector(lids_page.email_field_locator)
        lids_page.enter_email_address(email=get_data["emailid"])
        log.info("Entering the password")
        lids_page.enter_password(password=get_data["password"])
        log.info("Clicking the login button")
        profile_page = lids_page.click_login_button()
        log.info("Checking the presence of profile name locator after login")
        time.sleep(20)
        self.verify_element_presence_using_cssSelector(locator=ProfilePage.profile_name_field_locator)
        player_profile_name = profile_page.get_profile_name()
        log.info(f"Logged into {player_profile_name} account successfully")
        log.info("Current Page URL :"+self.driver.current_url)
        player_profile_url = self.driver.current_url
        profile_page.click_profile_setting_button()
        log.info("Clicked the setting button")
        profile_page.click_account_settings_button()
        log.info("Control in account settings page")
        player_url_identifier = profile_page.get_url_identifier()
        assert player_url_identifier in player_profile_url
        log.info("Verified the player URL identifier in the current URL of the PlayMaster page")
        profile_page.click_account_settings_close_button()
        time.sleep(3)
        log.info("Login to PlayMaster through email was successful")

    @pytest.fixture(params=LoginEmailData.test_login_email_data)
    def get_data(self, request):
        return request.param



