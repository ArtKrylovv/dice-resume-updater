from helpers.common import Common
from selenium.webdriver.common.by import By


class ProfilePage(Common):
    """
    Contains Profile page elements and action methods.
    """
    shadow_host = (By.CSS_SELECTOR, "dhi-candidates-wired-candidate-profile[class='theme-candidates hydrated']")
    button_edit_name = (By.CSS_SELECTOR, "button[aria-label='Edit Profile Banner']")
    field_first_name = (By.CSS_SELECTOR, "input[aria-label='First Name']")
    button_save_changes = (By.CSS_SELECTOR, "dhi-candidates-button[class='sc-dhi-candidates-candidate-profile-banner"
                                            "-edit sc-dhi-candidates-button-h sc-dhi-candidates-button-s hydrated']")
    text_last_update = (By.CSS_SELECTOR, "div[class='sc-dhi-candidates-candidate-profile-banner-view']")

    def __init__(self, driver):
        self.driver = driver

    def change_first_name(self, text):
        """
        This method takes text that holds new name value as an argument and calls
        group of methods that change first name.
        """
        self.click_button_edit_name()
        self.clear_field_first_name()
        self.input_first_name(text)
        self.click_button_save_changes()

    def click_button_edit_name(self):
        Common.wait_for_element_visible(self.driver, Common.find_shadow_element(self.driver, self.shadow_host,
                                                                                self.button_edit_name))
        Common.click_element(Common.find_shadow_element(self.driver, self.shadow_host, self.button_edit_name))

    def clear_field_first_name(self):
        field = Common.find_shadow_element(self.driver, self.shadow_host, self.field_first_name)
        Common.clear_field(field)

    def input_first_name(self, text):
        field = Common.find_shadow_element(self.driver, self.shadow_host, self.field_first_name)
        Common.field_input(field, text)

    def click_button_save_changes(self):
        button = Common.find_shadow_element(self.driver, self.shadow_host, self.button_save_changes)
        button.click()

    def get_last_update_value(self):
        el = Common.find_shadow_element(self.driver, self.shadow_host, self.text_last_update)
        return Common.get_el_text(el)

