from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CaseOneVotePage(BasePage):
    RADIO_BUTTON_SELECTOR = (By.CLASS_NAME, 'textCard')
    GUILTY_RADIO_BUTTON = (By.CSS_SELECTOR, '.question__body > div:nth-child(1)')
    VOTE_BUTTON = (By.CLASS_NAME, 'save_button')
    MODAL_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-dismiss="modal"]')
    MODAL_HEADER_TEXT = (By.CSS_SELECTOR, '.modal__header > div > div > div > h2 > strong')

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def click_guilty_radio_button(self):
        self.click_element(self.GUILTY_RADIO_BUTTON)

    def click_vote_button(self):
        self.click_element(self.VOTE_BUTTON)

    def assert_guilty_modal_header_text(self, expected_text):
        self.wait_for_element(self.MODAL_HEADER_TEXT)
        elements = self.find_elements(*self.MODAL_HEADER_TEXT)

        # Get text for first occurrence of modal header
        if elements:
            actual_text = elements[1].text
            assert actual_text == expected_text, f"MAJOR BUG: Popup modal is incorrectly displaying {actual_text}, when {expected_text} was selected"
        else:
            print("No elements found with data-dismiss='modal'")
