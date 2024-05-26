import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CaseSelectionPage:
    URL = 'https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a'

    def __init__(self, driver):
        self.driver = driver
        self.intro_text_locator = (By.CSS_SELECTOR, '[data-role="page.intro__text"]')

    def get_intro_text(self) -> str:
        return self.driver.find_element(*self.intro_text_locator).text


    def assert_intro_text_visible(self):
        try:
            # Wait for intro text to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.intro_text_locator)
            )
            logging.info("Case selection page intro text is visible.")
        except TimeoutException:
            raise AssertionError("Intro text is not visible on the page.")

