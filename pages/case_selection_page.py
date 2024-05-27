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
        self.case_selection_area = (By.CLASS_NAME, 'mod__bodycase_select')
        self.case = (By.CLASS_NAME, 'card')
        self.score = (By.XPATH, '//*[contains(text(), "Your score so far:")]')

    def assert_header_text(self, expected_text: str):
        # Wait until the header element is visible on the page
        header_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.header_text)
        )
        # Get the text from the header element
        actual_text = header_element.text
        assert expected_text == actual_text, f'Header text assertion failed: Expected text "{expected_text}" but got "{actual_text}"'


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

    def assert_case_selection_count(self, expected_count: int):
        # Locate the parent element
        parent_element = self.driver.find_element(self.case_selection_area)

        # Locate the child elements within the parent element
        child_elements = parent_element.find_elements(self.case)

        # Get the actual count of child elements
        actual_count = len(child_elements)

        # Perform the assertion
        assert actual_count == expected_count, f"Expected {expected_count} child elements, but found {actual_count}."

        print(f"Assertion passed: Found {actual_count} child elements, as expected.")

    def assert_score(self, expected_count: int):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.score)
        )
        full_text = element.text
        # Extract the desired part of the text using slicing
        partial_text = full_text[18:len(full_text)]

        print((partial_text))
        integer_number = int(partial_text)

        assert  integer_number == expected_count, f"Expected {expected_count} cases but found {integer_number}."