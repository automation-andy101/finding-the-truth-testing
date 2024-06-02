from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CaseVideoPage(BasePage):
    CASE_ONE_VIDEO_DESCRIPTION_TEXT = (By.XPATH, '//p/strong')
    CASE_TWO_VIDEO_DESCRIPTION_TEXT = (By.XPATH, '//p/strong[2]')
    VIDEO_TITLE = (By.CSS_SELECTOR, '[data-track-click="video-title"] > span')
    VIDEO_IFRAME = (By.TAG_NAME, 'iframe')
    CASE_ONE_VIDEO_TITLE = (By.XPATH, '//a/*[contains(text(), "Crime Myths - Case 1, Part 1")]')
    JUDGE_THIS_BUTTON = (By.CLASS_NAME, 'button--nav')

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def assert_case_video_title(self, expected_video_title):
        # Switch to the iframe containing the Vimeo video
        iframe = self.wait_for_element(self.VIDEO_IFRAME)
        self.driver.switch_to.frame(iframe)

        # Now you can search for elements within the iframe
        actual_text = self.get_element_text(self.VIDEO_TITLE)

        # Assert that actual video title matches what was expected
        assert expected_video_title == actual_text, (f"CRITICAL BUG: Incorrect video is being displayed on the page. "
                                                     f"Expected video with title '{expected_video_title}', "
                                                     f"but got '{actual_text}'")

    def assert_case_one_description_text_above_video(self, expected_description_text):
        # Switch back to the default content
        self.driver.switch_to.default_content()

        description_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CASE_ONE_VIDEO_DESCRIPTION_TEXT)
        )

        # Get the text of the first paragraph
        actual_text = description_text_element.text

        assert expected_description_text == actual_text, (f"MAJOR BUG: Incorrect video description text is being displayed "
                                                          f"on the page. Expected description t"
                                                          f"o contain '{expected_description_text}', "
                                                          f"but got '{actual_text}'")

    def assert_case_two_description_text_above_video(self, expected_description_text):
        # Switch back to the default content
        self.driver.switch_to.default_content()
        actual_text = self.get_element_text(self.CASE_TWO_VIDEO_DESCRIPTION_TEXT)

        assert actual_text in expected_description_text, (f"MAJOR BUG: Incorrect video description text is being displayed "
                                                          f"on the page")

    def click_judge_this_button(self):
        self.click_element(self.JUDGE_THIS_BUTTON)

