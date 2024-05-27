from behave import given, when, then
from utilities.configurations import *
from pages.landing_page import LandingPage

@given('I navigate to the Finding The Truth application')
def step_navigate_to_application(context):
    context.driver.maximize_window()
    context.driver.get(get_config()['TEST']['url'])

@given('I navigate to the case selection page')
def step_navigate_to_case_selection(context):
    context.driver.maximize_window()
    context.driver.get(get_config()['TEST']['url'])
    landing_page = LandingPage(context.driver)
    landing_page.click_start_button()

