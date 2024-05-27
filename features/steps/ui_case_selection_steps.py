from behave import given, when, then
from pages.landing_page import LandingPage
from pages.case_selection_page import CaseSelectionPage
from pages.case_video_page import CaseVideoPage


@then('case selection page header text is "{expected_text}"')
def step_assert_header_text(context, expected_text):
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.assert_case_selection_page_header_text(expected_text)


@then('page contains {number:d} cases to select from')
def step_assert_selectable_cases(context, number):
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.assert_case_selection_count(number)


@then('my score is "{expected_score}"')
def step_assert_expected_score(context, expected_score):
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.assert_score(expected_score)


@when('I click case {number:d}')
def step_click_case(context, number):
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.click_case_selector(number)


@then('I am navigated to a page containing a video titled "{expected_video_title}"')
def step_assert_case_one_video_title(context, expected_video_title):
    case_video_page = CaseVideoPage(context.driver)
    case_video_page.assert_case_video_title(expected_video_title)


@then('description text above case 1 video contains "{expected_description_text}"')
def step_assert_description_text(context, expected_description_text):
    case_video_page = CaseVideoPage(context.driver)
    case_video_page.assert_case_one_description_text_above_video(expected_description_text)


@then('description text above case 2 video contains "{expected_description_text}"')
def step_assert_description_text(context, expected_description_text):
    case_video_page = CaseVideoPage(context.driver)
    case_video_page.assert_case_two_description_text_above_video(expected_description_text)
