from behave import given, when, then
from pages.landing_page import LandingPage
from pages.case_selection_page import CaseSelectionPage

@when('I click the START button')
def step_click_start_button(context):
    landing_page = LandingPage(context.driver)
    landing_page.click_start_button()

@then('landing page is displayed containing header text "{expected_text}"')
def step_assert_header_text(context, expected_text):
    landing_page = LandingPage(context.driver)
    landing_page.assert_header_text(expected_text)

@then('image section is visible')
def step_assert_image_visible(context):
    landing_page = LandingPage(context.driver)
    landing_page.assert_image_element_is_visible()

@then('first paragraph text is "{expected_text}"')
def step_assert_first_paragraph_text(context, expected_text):
    landing_page = LandingPage(context.driver)
    landing_page.assert_first_paragraph_contains_expected_text(expected_text)

@then('second paragraph text is "{expected_text}"')
def step_assert_second_paragraph_text(context, expected_text):
    landing_page = LandingPage(context.driver)
    landing_page.assert_second_paragraph_contains_expected_text(expected_text)

@then('START button is visible')
def step_assert_start_button_visible(context):
    landing_page = LandingPage(context.driver)
    landing_page.assert_start_button_is_visible()

@then('I am navigated to the case selection page')
def step_verify_navigation_to_case_selection(context):
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.assert_intro_text_visible()


