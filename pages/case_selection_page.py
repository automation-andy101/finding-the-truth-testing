import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CaseSelectionPage:

    def __init__(self, driver):
        self.driver = driver
        self.header_text = (By.CSS_SELECTOR, '[data-role="page.name"] > strong')
        self.intro_text_locator = (By.CSS_SELECTOR, '[data-role="page.intro__text"]')
        self.case_selection_area = (By.CLASS_NAME, 'mod__body')
        self.case_selector = (By.CLASS_NAME, 'imageCard')
        self.case_one_selector = (By.XPATH, '//*[contains(text(), "Making a case against Kevin")]')
        self.score = (By.XPATH, '//*[contains(text(), "Your score so far:")]')


    def assert_case_selection_page_header_text(self, expected_text: str):
        # Wait until the header element is visible on the page
        header_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.header_text)
        )
        # Get the text from the header element
        actual_text = header_element.text
        print("ANDY - ", actual_text)
        assert expected_text == actual_text, f'Header text assertion failed: Expected text "{expected_text}" but got "{actual_text}"'


    def get_intro_text(self) -> str:
        # Wait for intro text to be visible
        intro_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*self.intro_text_locator)
        )
        return intro_text.text


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
        # Wait until the case selection area becomes visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.case_selection_area)
        )

        # Find number of case selectors cards on page
        case_selectors = self.driver.find_elements(*self.case_selector)

        # Count the number of elements
        actual_count = len(case_selectors)
        assert actual_count == expected_count, f"Expected {expected_count} selectable cases, but found {actual_count}."


    def assert_score(self, expected_score: str):
        score_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.score)
        )
        full_text = score_element.text
        print(full_text)
        # Extract the desired part of the text using slicing
        actual_score = full_text[18:len(full_text)]
        print(actual_score)

        assert actual_score == expected_score, f"Expected score to be {expected_score}, but score displayed on page is {actual_score}."

    def click_case_selector(self, number):
        # Wait until the case selection area becomes visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.case_selection_area)
        )
        case_selectors = self.driver.find_elements(*self.case_selector)

        # Check if there are any elements found
        if case_selectors:
            # Click on the first occurrence of the element
            case_selectors[number - 1].click()
            import time
            time.sleep(5)
        else:
            print("No cases found!!")

    def click_case_two_selector(self):
        # Wait until the case selection area becomes visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.case_selection_area)
        )
        case_selectors = self.driver.find_elements(*self.case_selector)

        # Check if there are any elements found
        if case_selectors:
            # Click on the second occurrence of the element
            case_selectors[1].click()
            import time
            time.sleep(5)
        else:
            print("No cases found!!")



