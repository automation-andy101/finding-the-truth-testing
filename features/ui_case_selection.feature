Feature: Case selection

    As a Finding the Truth user I want to be able to access the case selection page
    so that I can choose from a selection of cases to watch

    Background:
        Given I navigate to the case selection page

    Scenario: Case selection page loads and displays correct content
        Then case selection page header text is "FINDING THE TRUTH"
        And page contains 2 cases to select from
        And my score is "0"

    Scenario: Selecting case one
        When I click case one
        Then I am navigated to a page containing a video titled "Crime Myths - Case 1, Part 1"

    Scenario: Selecting case two
        When I click case two
        Then I am navigated to a page containing a video titled "Crime Myths - Case 2, Part 1"

