import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage:

    def __init__(self, driver):
        self.driver = driver
        self.header_text = (By.CLASS_NAME, 'projectTitle')
        self.image = (By.CLASS_NAME, 'image')
        self.paragraph_text_area = (By.CLASS_NAME, 'htmlText')
        self.first_paragraph_text = (By.XPATH, "//div[@class='htmlText']//p[1]")
        self.second_paragraph_text = (By.XPATH, "//div[@class='htmlText']//p[2]")
        self.start_btn = (By.CLASS_NAME, 'ti-chevron-right')


    def click_start_button(self):
        try:
            # Wait for the start button to be clickable
            start_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.start_btn)
            )
            # Click the start button
            start_button.click()
        except Exception as e:
            print(f"An error occurred while trying to click the start button: {e}")


    def assert_header_text(self, expected_text: str):
        # Wait until the header element is visible on the page
        header_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.header_text)
        )
        # Get the text from the header element
        actual_text = header_element.text
        assert expected_text == actual_text, f'Header text assertion failed: Expected text "{expected_text}" but got "{actual_text}"'


    def assert_image_element_is_visible(self):
        try:
            # Wait until the image is visible on the page
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.image)
            )
            logging.info("Image is visible.")
        except TimeoutException:
            raise AssertionError("Image is not visible on the page.")


    def assert_first_paragraph_contains_expected_text(self, expected_text):
        try:
            # Wait for the paragraph to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_paragraph_text))

            # Get the text of the first paragraph
            actual_text = self.driver.find_element(*self.first_paragraph_text).text

            # Assert whether the expected text is contained in the actual text
            assert expected_text in actual_text, f"Expected text '{expected_text}' not found in the first paragraph. Actual text: '{actual_text}'"
            logging.info(f"Sucessfully found expected text '{expected_text}' in the first paragraph.")
        except TimeoutException:
            logging.error("Timed out waiting for the first paragraph to be visible.")
        except AssertionError as e:
            logging.error(str(e))


    def assert_second_paragraph_contains_expected_text(self, expected_text):
        try:
            # Wait for the paragraph to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_paragraph_text))

            # Get the text of the first paragraph
            actual_text = self.driver.find_element(*self.first_paragraph_text).text

            # Assert whether the expected text is contained in the actual text
            assert expected_text in actual_text, f"Expected text '{expected_text}' not found in the second paragraph. Actual text: '{actual_text}'"
            logging.info(f"Sucessfully found expected text '{expected_text}' in the first paragraph.")
        except TimeoutException:
            logging.error("Timed out waiting for the second paragraph to be visible.")
        except AssertionError as e:
            logging.error(str(e))


    def assert_start_button_is_visible(self):
        try:
            # Wait for the paragraph to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.start_btn)
            )
            logging.info("START button is visible.")

        except TimeoutException:
            raise AssertionError("START button is not visible on the page.")


