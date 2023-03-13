from pom.login_page import LoginPage
from pom.profile_page import ProfilePage
from pom.home_page import HomePage


class BasePage:
    """
    Provides access to all page elements and action methods.
    """
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.home_page = HomePage(driver)
