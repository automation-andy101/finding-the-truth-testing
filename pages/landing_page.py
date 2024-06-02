from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LandingPage(BasePage):
    HEADER_TEXT = (By.CSS_SELECTOR, '[data-role="project.name"]')
    IMAGE = (By.CLASS_NAME, 'image')
    PARAGRAPH_TEXT_AREA = (By.CLASS_NAME, 'htmlText')
    FIRST_PARAGRAPH_TEXT = (By.XPATH, "//div[@class='htmlText']//p[1]")
    SECOND_PARAGRAPH_TEXT = (By.XPATH, "//div[@class='htmlText']//p[2]")
    START_BUTTON = (By.CLASS_NAME, 'ti-chevron-right')

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def click_start_button(self):
        self.click_element(self.START_BUTTON)

    def assert_landing_page_header_text(self, expected_text: str):
        actual_text = self.get_element_text(self.HEADER_TEXT)
        assert expected_text == actual_text, (
            f'MINOR BUG: Header text assertion failed: Expected text "{expected_text}" '
            f'but got "{actual_text}"')

    def assert_image_element_is_visible(self):
        assert self.is_element_visible(self.IMAGE), f"MINOR BUG: Image is not visible on the page."

    def assert_first_paragraph_contains_expected_text(self, expected_text):
        actual_text = self.get_element_text(self.FIRST_PARAGRAPH_TEXT)

        # Assert whether the expected text is contained in the actual text
        assert expected_text in actual_text, (f"MINOR BUG: Expected text '{expected_text}' not found in the first "
                                              f"paragraph. Actual text: '{actual_text}'")

    def assert_second_paragraph_contains_expected_text(self, expected_text):
        actual_text = self.get_element_text(self.SECOND_PARAGRAPH_TEXT)

        # Assert whether the expected text is contained in the actual text
        assert expected_text in actual_text, (f"MINOR BUG: Expected text '{expected_text}' not found in the second "
                                              f"paragraph. Actual text: '{actual_text}'")

    def assert_start_button_is_visible(self):
        assert self.is_element_visible(self.IMAGE), "CRITICAL BUG: START button is not visible on the page."
