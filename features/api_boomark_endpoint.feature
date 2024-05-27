@exclude_before_all
Feature: [API TEST] Finding The Truth Bookmark Endpoint Testing

    As a user of the Finding The Truth bookmark service,
    I want to ensure that the bookmark endpoint functions correctly,
    So that I can manage my bookmarks effectively.

    Scenario: Fetch bookmark history for a new user session
        When I send a GET request to the bookmark endpoint for a new user session
        Then the response status code is 200
        And the response body only contain history for the bookmark with ID "5c9126fe3b767"


    Scenario: Send bookmark history for a new user session to server
        Given I have a valid bookmark history payload for a new user session
        When I send a POST request to the bookmark endpoint for a new user session
        Then the response status code is 204



