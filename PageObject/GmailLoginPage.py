import time

from selenium.webdriver.common.by import By

from PageObject.ProfilePage import ProfilePage


class GmailLoginPage:
    email_field_locator = "input#identifierId"
    email_field = (By.CSS_SELECTOR, "input#identifierId")
    next_button_locator = "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b"
    next_button = (By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b")
    password_field = (By.CSS_SELECTOR, "input[type='password']")

    def __init__(self, driver):
        self.driver = driver

    def enter_gmail_address(self, gmail):
        return self.driver.find_element(*GmailLoginPage.email_field).send_keys(gmail)

    def click_next_button(self):
        return self.driver.find_element(*GmailLoginPage.next_button).click()

    def enter_gmail_password(self, password):
        return self.driver.find_element(*GmailLoginPage.password_field).send_keys(password)

    def click_final_next_button(self):
        self.driver.find_element(*GmailLoginPage.next_button).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile_page = ProfilePage(self.driver)
        return profile_page
