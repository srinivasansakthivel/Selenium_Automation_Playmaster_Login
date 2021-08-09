import time

from selenium.webdriver.common.by import By


class ProtonEmailPage:
    proton_homepage_login_button = (By.XPATH, "//a[contains(text(),'LOG IN')]")
    proton_sign_in_button_locator = "//button[contains(text(),'Sign in')]"
    proton_sign_in_button = (By.XPATH, proton_sign_in_button_locator)
    proton_username_field = (By.XPATH, "//input[@id='username']")
    proton_password_field = (By.XPATH, "//input[@id='password']")
    proton_header_locator = "//header/div[1]/a[1]"
    proton_twitch_email_header = (By.XPATH, "//span[contains(text(),'Your Twitch Login Verification Code')]")
    proton_twitch_email_count = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/div/div[2]/div/div[2]/div[1]/span[1]")
    proton_reset_password_email_header = (By.XPATH, "//span[contains(text(),'Reset your Logi ID password')]")
    proton_reset_password_email_count = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/div/div["
                                                   "2]/div/div[2]/div[1]/span[1]")

    def __init__(self, driver):
        self.driver = driver

    def click_proton_homepage_login_button(self):
        return self.driver.find_element(*ProtonEmailPage.proton_homepage_login_button).click()

    def enter_proton_email_username(self, username):
        return self.driver.find_element(*ProtonEmailPage.proton_username_field).send_keys(username)

    def enter_proton_email_password(self, password):
        return self.driver.find_element(*ProtonEmailPage.proton_password_field).send_keys(password)

    def click_proton_email_sign_in_button(self):
        return self.driver.find_element(*ProtonEmailPage.proton_sign_in_button).click()

    def click_proton_twitch_email_header(self):
        return self.driver.find_element(*ProtonEmailPage.proton_twitch_email_header).click()

    def get_proton_twitch_email_passcode(self):
        email_count = self.driver.find_element(*ProtonEmailPage.proton_twitch_email_count).text
        email_count_str = str(email_count)
        exact_email_count = email_count_str[1:-1]
        time.sleep(5)
        message_locator = self.driver.find_element(By.XPATH, "//body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/main["
                                                             "1]/section[1]/div[1]/div[1]/article[%s]/div[2]" % str(exact_email_count))
        message_locator.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", message_locator)
        time.sleep(2)
        last_email_code = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div["
                                                            "1]/main[1]/section[1]/div[1]/div[1]/article[%s]/div["
                                                            "2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody["
                                                            "1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/table["
                                                            "1]/tbody[1]/tr[4]/td[1]/div[2]" % str(exact_email_count)).text
        return last_email_code

    def close_proton_email_page(self):
        self.driver.close()
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def click_reset_password_email_header(self):
        return self.driver.find_element(*ProtonEmailPage.proton_reset_password_email_header).click()

    def click_reset_password_link(self):
        email_count = self.driver.find_element(*ProtonEmailPage.proton_reset_password_email_count).text
        email_count_str = str(email_count)
        exact_email_count = email_count_str[1:-1]
        # exact_email_count_int = int(exact_email_count_str)
        # exact_email_count = str(exact_email_count_int-1)
        time.sleep(4)
        message_locator = self.driver.find_element(By.XPATH, "//body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/main["
                                                             "1]/section[1]/div[1]/div[1]/article[%s]/div[2]" % str(exact_email_count))
        message_locator.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", message_locator)
        time.sleep(1)
        reset_password_link_locator = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[1]/div["
                                                                        "2]/div[1]/main[1]/section[1]/div[1]/div["
                                                                        "1]/article[%s]/div[2]/div[1]/table[3]/tbody["
                                                                        "1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td["
                                                                        "1]/table[1]/tbody[1]/tr[6]/td[1]/table["
                                                                        "1]/tbody[1]/tr[1]/td[1]" % str(exact_email_count))
        # self.driver.execute_script("arguments[0].scrollIntoView();", reset_password_link_locator)
        reset_password_link_locator.click()
        time.sleep(2)
