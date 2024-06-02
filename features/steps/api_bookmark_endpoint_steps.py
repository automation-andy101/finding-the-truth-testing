import requests
import uuid
from behave import given, when, then
from utilities.api_requests import APIClient
from utilities.configurations import get_api_config
from payloads.payloads import *

# Session UUID
session_uuid = None

@given('I have a valid bookmark history payload for a new user session')
def step_valid_bookmark_history_payload_for_ne_user_session(context):
    context.bookmark_payload = new_user_session_bookmark_history_json()


@when("I send a GET request to the bookmark endpoint for a new user session")
def step_send_GET_request_to_bookmark_endpoint_for_new_user_session(context):
    global session_uuid
    # Generate a new UUID
    session_uuid = str(uuid.uuid4())

    username = get_api_config()['TEST']['API_ADMIN_USERNAME']
    password = get_api_config()['TEST']['API_ADMIN_PASSWORD']

    bearer_token = APIClient().get_bearer_token(username, password)
    context.response = APIClient().get_bookmarks(bearer_token, session_uuid)


@when("I send a POST request to the bookmark endpoint for a new user session")
def step_send_POST_request_to_bookmark_endpoint_for_new_user_session(context):
    global session_uuid
    # Generate a new UUID
    session_uuid = str(uuid.uuid4())

    username = get_api_config()['TEST']['API_ADMIN_USERNAME']
    password = get_api_config()['TEST']['API_ADMIN_PASSWORD']

    bearer_token = APIClient().get_bearer_token(username, password)
    payload = new_user_session_bookmark_history_json()
    context.response = APIClient().post_bookmarks(bearer_token, session_uuid, payload)


@then('the response status code is {expected_status_code:d}')
def step_status_code_should_be(context, expected_status_code):
    assert context.response.status_code == expected_status_code, \
        f"Expected status code {expected_status_code} but got {context.response.status_code}"


@then('the response body only contain history for the bookmark with ID {expected_bookmark_id}')
def step_bookmark_history_response_contains_id(context, expected_bookmark_id):
    response_json = context.response()

    assert isinstance(response_json, dict), f"Response JSON is not a dictionary: {response_json}"

    # Check the nested structure in 'history'
    history = response_json["history"]
    assert len(history) == 1, f"Expected history to have one item, but got {len(history)}"
    assert expected_bookmark_id in history, f"Expected history to contain the key '{expected_bookmark_id}', but it does not"


