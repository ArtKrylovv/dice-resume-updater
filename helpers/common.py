import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
from utilities import config


class Common:
    """
    Contains common selenium as well as project specific methods.
    """
    @staticmethod
    def setup(headless):
        options = Options()
        options.headless = headless
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options)
        # this statement ensures sufficient window size when running browser in headless mode
        if config.get_data()['headless']:
            driver.set_window_size(2560, 1600)
        else:
            driver.maximize_window()
        driver.implicitly_wait(3)
        return driver

    @staticmethod
    def teardown(driver):
        driver.quit()

    @staticmethod
    def navigate_to_url(driver, url):
        driver.get(url)

    @staticmethod
    def find_element(driver, locator):
        el = driver.find_element(*locator)
        return el

    @staticmethod
    def click_element(el):
        el.click()

    @staticmethod
    def field_input(el, text):
        el.send_keys(text)

    @staticmethod
    def find_shadow_element(driver, shadow_host_locator, el_locator):
        shadow_host = driver.find_element(*shadow_host_locator)
        shadow_root = shadow_host.shadow_root
        el = shadow_root.find_element(*el_locator)
        return el

    @staticmethod
    def clear_field(el):
        el.clear()

    # this method checks creates screenshots directory, gets and stores driver screenshots
    @staticmethod
    def get_screenshot(driver, time, status):
        if not os.path.exists('./screenshots'):
            os.makedirs('./screenshots')
        driver.save_screenshot(f'./screenshots/Job_{status}_{time}.png')

    # this method gets current time that is used in screenshot .png files name
    @staticmethod
    def get_current_time():
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%B %d, %Y %H:%M:%S")
        return formatted_time

    @staticmethod
    def get_el_text(el):
        return el.text

    @staticmethod
    def wait_for_element_visible(driver, el):
        wait = WebDriverWait(driver, 3)
        wait.until(ec.visibility_of(el))