from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)


    def find_element(self, *locator):
        self.logger.info(f"Finding element with locator: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.logger.info(f"Finding elements with locator: {locator}")
        return self.driver.find_elements(*locator)

    def click_element(self, *locator):
        self.logger.info(f"Clicking element with locator: {locator}")
        element = self.wait_for_element(*locator)
        element.click()

    def send_keys(self, keys, *locator):
        self.logger.info(f"Sending keys '{keys}' to element with locator: {locator}")
        element = self.find_element(*locator)
        element.send_keys(keys)

    def wait_for_element(self, *locator):
        self.logger.info(f"Waiting for element with locator: {locator}")
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(*locator)
            )
            return element
        except TimeoutException:
            self.logger.info(f"Element with locator {locator} did not appear within {self.timeout} seconds")
            return None

    def is_element_visible(self, *locator):
        self.logger.info(f"Checking visability of element with locator: {locator}")
        element = self.wait_for_element(*locator)
        return element.is_displayed() if element else False

    def get_element_text(self, *locator):
        self.logger.info(f"Getting text of element with locator: {locator}")
        element = self.wait_for_element(*locator)
        if element:
            try:
                text = element.text
                self.logger.info(f"Text of element with locator {locator} is: {text}")
                return text
            except NoSuchElementException:
                self.logger.error(f"Element with locator {locator} is not found")
                return None
        else:
            self.logger.error(f"Element with locator {locator} is not found")
            return None

