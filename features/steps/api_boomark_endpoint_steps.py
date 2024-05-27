import requests
from behave import given, when, then
import uuid

# Session UUID
session_uuid = None

@when("I send a GET request to the bookmark endpoint for a new user session")
def step_send_GET_request_to_bookmark_endpoint_for_new_user_session(context):
    global session_uuid
    # Generate a new UUID
    session_uuid = str(uuid.uuid4())
    print("Generated UUID:", session_uuid)

    response = requests.get(f"{BASE_URL}/ap_bookmark_endpoint/{bookmark_id}", json=context.updated_payload)
    context.response = response

