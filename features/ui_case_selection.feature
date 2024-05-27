Feature: Case selection

    As a Finding the Truth user I want to be able to access the case selection page
    so that I can choose from a selection of cases to watch

    Background:
        Given I navigate to the case selection page

    Scenario: Case selection page loads and displays correct content
        Then case selection page header text is "FINDING THE TRUTH"
        And page contains 2 cases to select from
        And my score is 0

    Scenario: Selecting case one
        When I click the 'Making a case against Kevin' case area
        Then I am navigated to a page containing a video titled "Crime Myths - Case 1, Part 1"
        And text above video is "A murder has been committed in an alleyway outside a pub."

    Scenario: Selecting case two
        When I click the 'Who is to blame?' case area
        Then I am navigated to a page containing a video title "Crime Myths - Case 2, Part 1"
        And text above video is "A young man has been in an accident in the warehouse where he worked and has subsequently died.


