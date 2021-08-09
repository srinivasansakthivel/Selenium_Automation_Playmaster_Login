import time

import pytest

from PageObject.LidsPage import LidsPage
from PageObject.LoginPage import LoginPage
from PageObject.ProtonEmailPage import ProtonEmailPage
from TestData.ForgotPasswordEmailData import ForgotPasswordEmailData
from utilities.BaseClass import BaseClass


class TestForgotEmailPassword(BaseClass):

    def test_forget_email_password(self, get_data):
        log = self.getlogger()
        log.info("Created logger object from baseclass")
        log.info("Creating login page object, login_page")
        login_page = LoginPage(self.driver)
        log.info("Title of the PlayMaster Page" + self.driver.title)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "PLAYMASTER - CS:GO Training and Skills Practice"
        log.info("Verified the Title of the PlayMaster Page")
        log.info("Protonmail Page URL : " + self.driver.current_url)
        log.info("Checking the present of early access sign-in button")
        self.verify_element_presence_using_cssSelector(login_page.early_access_signup_button_locator)
        lids_page = login_page.click_early_access_sign_button()
        time.sleep(3)
        log.info("Checking the present of 'Forget Password?' link text")
        lids_page.click_forget_password_link()
        time.sleep(3)
        log.info("Clicked on 'Forget Password?' link")
        log.info("Title of the Forgot Password Page" + self.driver.title)
        log.info("Forgot Password Page URL : " + self.driver.current_url)
        self.verify_element_presence_using_cssSelector(lids_page.request_reset_button_locator)
        log.info("Verified the presence of Request Reset Button in the Forgot Password Page")
        lids_page.request_reset_password(email=get_data["emailid"])
        time.sleep(30)
        assert self.driver.find_element_by_xpath(lids_page.forgot_password_status_area).is_displayed()
        log.info("Verified the 'password reset link sent to email' popup message")
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://protonmail.com/")
        proton_email_page = ProtonEmailPage(self.driver)
        log.info("Title of the Protonmail Page" + self.driver.title)
        log.info("Protonmail Page URL : " + self.driver.current_url)
        proton_email_page.click_proton_homepage_login_button()
        log.info("Clicked the login button in the proton home page")
        self.verify_element_presence_using_xpath(proton_email_page.proton_sign_in_button_locator)
        time.sleep(3)
        log.info("Verified the presence of login button in the Enter User Credentials - Proton login Page")
        proton_email_page.enter_proton_email_username(username=get_data["emailid"])
        log.info("Enter the username in the proton email login page")
        proton_email_page.enter_proton_email_password(password=get_data["email_password"])
        log.info("Entered the password in the proton email login page")
        proton_email_page.click_proton_email_sign_in_button()
        log.info("Clicked the Sign in button in the proton email login page")
        time.sleep(6)
        self.verify_element_presence_using_xpath(proton_email_page.proton_header_locator)
        log.info("logged into protonmail successfully")
        proton_email_page.click_reset_password_email_header()
        time.sleep(5)
        proton_email_page.click_reset_password_link()
        log.info("Clicked the reset password link")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)
        lids_page = LidsPage(self.driver)
        lids_page.update_email_password(new_password=get_data["new_password"])
        time.sleep(3)
        assert self.driver.find_element_by_xpath(lids_page.password_reset_successful_locator).is_displayed()
        log.info("Verified the Password Reset Successful Message")
        # password_reset_successful_message = self.driver.find_element_by_xpath(lids_page.password_reset_successful_locator).text
        # assert "Password Reset Successful" in password_reset_successful_message

        # reset_password_message = reset_password_message_locator.text
        # # reset_password_message = self.driver.execute_script("arguments[0].value", reset_password_message_locator)
        # log.info("Message :"+reset_password_message)
        # assert "password reset link will be sent to your inbox" in reset_password_message

    @pytest.fixture(params=ForgotPasswordEmailData.test_forgot_password_email_data)
    def get_data(self, request):
        return request.param
