import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CaseVideoPage:

    def __init__(self, driver):
        self.driver = driver
        self.video_description_text = (By.XPATH, '//p/strong')
        # self.video_description_text_locator = (By.TAG_NAME, 'strong')
        self.video_iframe = (By.TAG_NAME, 'iframe')
        self.case_one_video_title = (By.XPATH, '//a/*[contains(text(), "Crime Myths - Case 1, Part 1")]')


    def assert_case_one_video_title(self, expected_video_title: str):
        try:
            # Switch to the iframe containing the Vimeo video
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.video_iframe))
            self.driver.switch_to.frame(iframe)

            # Now you can search for elements within the iframe
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.case_one_video_title)
            )

            # Assert that the element is visible or exists
            assert element.is_displayed(), "Video title element is not visible or does not exist in the DOM"
            logging.info(f"'{expected_video_title}' video title is visible.")
        except TimeoutException:
            raise AssertionError(f"Incorrect video is being displayed on the page. Expected video with title '{expected_video_title}'")


    def assert_case_video_title(self, expected_video_title: str):
        try:
            # Switch to the iframe containing the Vimeo video
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.video_iframe))
            self.driver.switch_to.frame(iframe)

            # Now you can search for elements within the iframe
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.case_one_video_title)
            )

            # Assert that the element is visible or exists
            assert element.is_displayed(), "Video title element is not visible or does not exist in the DOM"
            logging.info(f"'{expected_video_title}' video title is visible.")
        except TimeoutException:
            raise AssertionError(f"Incorrect video is being displayed on the page. Expected video with title '{expected_video_title}'")

