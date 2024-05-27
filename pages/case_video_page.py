from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CaseVideoPage:

    def __init__(self, driver):
        self.driver = driver
        self.case_one_video_description_text = (By.XPATH, '//p/strong')
        self.case_two_video_description_text = (By.XPATH, '//p/strong[2]')
        self.video_title = (By.CSS_SELECTOR, '[data-track-click="video-title"] > span')
        self.video_iframe = (By.TAG_NAME, 'iframe')
        self.case_one_video_title = (By.XPATH, '//a/*[contains(text(), "Crime Myths - Case 1, Part 1")]')

    def assert_case_video_title(self, expected_video_title: str):
        # Switch to the iframe containing the Vimeo video
        iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.video_iframe))
        self.driver.switch_to.frame(iframe)

        # Now you can search for elements within the iframe
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.video_title)
        )
        actual_text = element.text

        # Assert that actual video title matches what was expected
        assert expected_video_title == actual_text, (f"CRITICAL BUG: Incorrect video is being displayed on the page. "
                                                     f"Expected video with title '{expected_video_title}', "
                                                     f"but got '{actual_text}'")

    def assert_case_one_description_text_above_video(self, expected_description_text: str):
        # Switch back to the default content
        self.driver.switch_to.default_content()

        description_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.case_one_video_description_text)
        )

        # Get the text of the first paragraph
        actual_text = description_text_element.text

        assert expected_description_text == actual_text, (f"MAJOR BUG: Incorrect video description text is being displayed "
                                                          f"on the page. Expected description t"
                                                          f"o contain '{expected_description_text}', "
                                                          f"but got '{actual_text}'")

    def assert_case_two_description_text_above_video(self, expected_description_text: str):
        # Switch back to the default content
        self.driver.switch_to.default_content()

        description_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.case_two_video_description_text)
        )

        actual_text = description_text_element.text

        assert actual_text in expected_description_text, (f"MAJOR BUG: Incorrect video description text is being displayed "
                                                          f"on the page")
