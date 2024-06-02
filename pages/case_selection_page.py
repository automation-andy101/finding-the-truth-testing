from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CaseSelectionPage(BasePage):
    HEADER_TEXT = (By.CSS_SELECTOR, '[data-role="page.name"] > strong')
    INTRO_TEXT_LOCATOR = (By.CSS_SELECTOR, '[data-role="page.intro__text"]')
    CASE_SELECTION_AREA = (By.CLASS_NAME, 'mod__body')
    CASE_SELECTOR = (By.CLASS_NAME, 'imageCard')
    CASE_ONE_SELECTOR = (By.XPATH, '//*[contains(text(), "Making a case against Kevin")]')
    SCORE = (By.XPATH, '//*[contains(text(), "Your score so far:")]')

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def assert_case_selection_page_header_text(self, expected_text: str):
        actual_text = self.get_element_text(self.HEADER_TEXT)
        assert expected_text == actual_text, (
            f'MINOR BUG: Header text assertion failed: Expected text "{expected_text}" '
            f'but got "{actual_text}"')

    def assert_intro_text_visible(self):
        assert self.is_element_visible(self.INTRO_TEXT_LOCATOR), f"MINOR BUG: Intro text is not visible on the page."

    def assert_case_selection_count(self, expected_count: int):
        # Wait until the case selection area becomes visible
        self.wait_for_element(self.CASE_SELECTION_AREA)

        # Find number of case selectors cards on page
        case_selectors = self.find_elements(*self.CASE_SELECTOR)
        actual_count = len(case_selectors)
        assert actual_count == expected_count, f"MAJOR BUG: Expected {expected_count} selectable cases, but found {actual_count}."

    def assert_score(self, expected_score: str):
        full_text = self.get_element_text(self.SCORE)
        # Extract the desired part of the text using slicing
        actual_score = full_text[18:len(full_text)]
        assert actual_score == expected_score, (
            f"MAJOR BUG: Incorrect Score! Expected score to be {expected_score}, but "
            f"score displayed on page is {actual_score}.")

    def click_case_selector(self, number):
        self.wait_for_element(self.CASE_SELECTION_AREA)
        case_selectors = self.find_elements(*self.CASE_SELECTOR)

        # Check if there are any elements found
        if case_selectors:
            # Click on the first occurrence of the element
            case_selectors[number - 1].click()
        else:
            print("No cases found!!")

    def click_case_two_selector(self):
        self.wait_for_element(self.CASE_SELECTION_AREA)
        case_selectors = self.find_elements(*self.CASE_SELECTOR)

        # Check if there are any elements found
        if case_selectors:
            # Click on the second occurrence of the element
            case_selectors[1].click()
        else:
            print("No cases found!!")
