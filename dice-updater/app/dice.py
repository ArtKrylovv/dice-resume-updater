from selenium.common import NoSuchElementException
from pom import base_page
from helpers import common
from utilities import config
from utilities.logger import get_logger


def dice_update(max_attempts, headless):
    """
    Function updates Dice profile by changing first name to dummy name and back.
    To ensure profile has been updated function asserts text value of web element equals 'Today' and gets screenshot.
    In case NoSuchElement error script gets screenshot and executes job until max number of attempts is reached.

    """
    logger = get_logger()
    attempt, success = 1, False
    while attempt <= max_attempts and not success:
        try:
            print(f'>>> executing job attempt # {attempt}')
            logger.debug(f'executing setup for attempt #{attempt}')
            driver = common.Common.setup(headless)

            logger.debug('navigating to login page')
            page = base_page.BasePage(driver)
            page.login_page.navigate_to_login_page()

            logger.debug('loging in')
            page.login_page.input_email(config.get_data()['email'])
            page.login_page.input_password(config.get_data()['password'])
            page.login_page.click_submit()

            logger.debug('navigating to profile page')
            page.home_page.click_link_profile()

            logger.debug('updating first name to dummy value')
            page.profile_page.change_first_name(config.get_data()['dummy_name'])

            logger.debug('updating first name back to real value')
            page.profile_page.change_first_name(config.get_data()['real_name'])

            logger.debug('asserting last update text value equals "Today"')
            actual_value = page.profile_page.get_last_update_value()
            expected_value = 'Today'
            assert expected_value in actual_value

            print(f'>>> job execution successful ✅✅✅\n>>> you can find job screenshot at "/screenshots" directory ')
            logger.debug('getting job success screenshot')
            common.Common.get_screenshot(driver, common.Common.get_current_time(), 'success')

            logger.debug('executing teardown')
            common.Common.teardown(driver)
            success = True

        except NoSuchElementException:
            print(f'>>> job execution failed ❌❌❌')
            logger.error('getting job failure screenshot')
            common.Common.get_screenshot(driver, common.Common.get_current_time(), 'failure')
            logger.debug('executing teardown')
            common.Common.teardown(driver)
            attempt += 1


