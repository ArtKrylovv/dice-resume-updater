from helpers.common import Common
from selenium.webdriver.common.by import By


class LoginPage(Common):
    """
    Contains Login page url, elements and action methods.
    """
    url = 'https://www.dice.com/dashboard/login'
    field_email = (By.ID, 'email')
    field_password = (By.ID, 'password')
    button_submit = (By.XPATH, '//button[@type = "submit"]')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        Common.navigate_to_url(self.driver, LoginPage.url)

    def input_email(self, text):
        Common.field_input(Common.find_element(self.driver, self.field_email), text)

    def input_password(self, text):
        Common.field_input(Common.find_element(self.driver, self.field_password), text)

    def click_submit(self):
        Common.click_element(Common.find_element(self.driver, self.button_submit))
