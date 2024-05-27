from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CaseOneVotePage:

    def __init__(self, driver):
        self.driver = driver
        self.radio_button_selector = (By.CLASS_NAME, 'textCard')
        self.guilty_radio_button = (By.CSS_SELECTOR, '.question__body > div:nth-child(1)')
        self.vote_button = (By.CLASS_NAME, 'save_button')
        self.modal_continue_button = (By.CSS_SELECTOR, '[data-dismiss="modal"]')
        self.modal_header_text = (By.CSS_SELECTOR, '.modal__header > div > div > div > h2 > strong')

    def click_guilty_radio_button(self):
        # Wait until the radio buttons becomes visible
        radio_button_selectors = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.guilty_radio_button)
        )
        radio_button_selectors.click()

    def click_vote_button(self):
        # Wait until the vote button becomes visible
        vote_button_selectors = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.vote_button)
        )
        vote_button_selectors.click()

    def assert_guilty_modal_header_text(self, expected_text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.modal_header_text)
        )
        elements = self.driver.find_elements(*self.modal_header_text)

        # Get text for first occurrence of modal header
        if elements:
            actual_text = elements[1].text
            assert actual_text == expected_text, f"MAJOR BUG: Popup modal is incorrectly displaying {actual_text}, when {expected_text} was selected"
        else:
            print("No elements found with data-dismiss='modal'")
