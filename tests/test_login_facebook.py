import time
import pytest
from PageObject.LoginPage import LoginPage
from TestData.LoginFacebookData import LoginFacebookData
from utilities.BaseClass import BaseClass
from PageObject.ProfilePage import ProfilePage


class TestLoginFacebook(BaseClass):

    def test_login_facebook(self, get_data):
        log = self.getlogger()
        log.info("Created logger object from baseclass")
        log.info("Creating login page object, login_page")
        login_page = LoginPage(self.driver)
        log.info("Current Page Title : "+self.driver.title)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "PLAYMASTER - CS:GO Training and Skills Practice"
        log.info("Current Page URL :"+self.driver.current_url)
        log.info("Checking the present of early access sign-in button")
        self.verify_element_presence_using_cssSelector(login_page.early_access_signup_button_locator)
        lids_page = login_page.click_early_access_sign_button()
        time.sleep(3)
        log.info("Checking the present of facebook button")
        self.verify_element_presence_using_cssSelector(lids_page.facebook_button_locator)
        facebook_login_page = lids_page.click_facebook_button()
        log.info("Clicked the facebook button")
        self.verify_element_presence_using_cssSelector(facebook_login_page.facebook_login_button_locator)
        time.sleep(2)
        log.info("Current Page URL :"+self.driver.current_url)
        facebook_login_page.enter_facebook_email(email=get_data["emailid"])
        log.info("Entered the facebook email address")
        facebook_login_page.enter_facebook_password(password=get_data["password"])
        log.info("Enter the facebook password")
        profile_page = facebook_login_page.click_facebook_login_button()
        log.info("Clicked the facebook login button")
        log.info("Checking the presence of profile name locator after login")
        time.sleep(15)
        self.verify_element_presence_using_cssSelector(locator=ProfilePage.profile_name_field_locator)
        player_profile_name = profile_page.get_profile_name()
        log.info(f"Logged into {player_profile_name} account successfully")
        log.info("Current Page URL :"+self.driver.current_url)
        player_profile_url = self.driver.current_url
        profile_page.click_profile_setting_button()
        log.info("Clicked the setting button")
        time.sleep(1)
        profile_page.click_account_settings_button()
        log.info("Control in account settings page")
        player_url_identifier = profile_page.get_url_identifier()
        assert player_url_identifier in player_profile_url
        log.info("Verified thr player URL identifier in the current URL of the page")
        profile_page.click_account_settings_close_button()
        time.sleep(3)
        log.info("Logged into PlayMaster successful through Facebook successfully")

    @pytest.fixture(params=LoginFacebookData.test_login_facebook_data)
    def get_data(self, request):
        return request.param
