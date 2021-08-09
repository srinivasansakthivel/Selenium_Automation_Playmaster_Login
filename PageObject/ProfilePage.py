from selenium.webdriver.common.by import By


class ProfilePage:
    profile_name_field_locator = ".username___3ERcP"
    profile_name_field = (By.CSS_SELECTOR, ".username___3ERcP")
    profile_setting_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/span/img")
    account_settings_button = (By.XPATH, "//span[contains(text(),'Account Settings')]")
    url_identifier_field = (By.CSS_SELECTOR, "input[placeholder='URL ID']")
    account_settings_close_button = (By.CSS_SELECTOR, ".close-btn___2yE7n")
    profile_pm_header_locator = "div.header-title-logo___1NGSA"
    profile_access_code_field_locator = "input[name='access_key']"
    profile_access_code_continue_button_locator = "button[type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_profile_setting_button(self):
        return self.driver.find_element(*ProfilePage.profile_setting_button).click()

    def get_profile_name(self):
        return self.driver.find_element(*ProfilePage.profile_name_field).text

    def click_account_settings_button(self):
        return self.driver.find_element(*ProfilePage.account_settings_button).click()

    def get_url_identifier(self):
        return self.driver.find_element(*ProfilePage.url_identifier_field).text

    def click_account_settings_close_button(self):
        return self.driver.find_element(*ProfilePage.account_settings_close_button).click()

