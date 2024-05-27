from behave import given, when, then
from pages.landing_page import LandingPage
from utilities.configurations import *
from pages.case_selection_page import CaseSelectionPage
from pages.case_video_page import CaseVideoPage
from pages.case_one_Vote_page import CaseOneVotePage

@given('I have selected case one')
def step_select_case_one(context):
    context.driver.maximize_window()
    context.driver.get(get_config()['TEST']['url'])
    landing_page = LandingPage(context.driver)
    landing_page.click_start_button()
    case_selection_page = CaseSelectionPage(context.driver)
    case_selection_page.click_case_selector(1)

@given('I click the JUDGE THIS button under the video')
def step_click_judge_button_under_video(context):
    case_video_page = CaseVideoPage(context.driver)
    case_video_page.click_judge_this_button()


@when('I select the Guilty radio button')
def step_select_guilty_radio_button(context):
    case_one_vote_page = CaseOneVotePage(context.driver)
    case_one_vote_page.click_guilty_radio_button()


@when('click the VOTE button')
def step_click_the_vote_button(context):
    case_one_vote_page = CaseOneVotePage(context.driver)
    case_one_vote_page.click_vote_button()


@then('popup modal appears stating "{expected_text}"')
def step_assert_modal_text_is_guilty(context, expected_text):
    case_one_vote_page = CaseOneVotePage(context.driver)
    case_one_vote_page.assert_guilty_modal_header_text(expected_text)


