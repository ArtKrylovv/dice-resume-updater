from helpers.common import Common
from selenium.webdriver.common.by import By


class HomePage(Common):
    """
    Contains Home page elements and action methods.
    """
    link_profile = (By.CSS_SELECTOR, '#profileLink')

    def __init__(self, driver):
        self.driver = driver

    def click_link_profile(self):
        Common.click_element(Common.find_element(self.driver, self.link_profile))
