import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        return logger

    def verify_element_presence_using_linkText(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, locator)))

    def verify_element_presence_using_xpath(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, locator)))

    def verify_element_presence_using_cssSelector(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def verify_element_presence_using_className(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, locator)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        return dropdown.select_by_visible_text(text)
