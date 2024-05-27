Feature: Finding The Truth Bookmark Endpoint Testing

    As a user of the bookmark service,
    I want to ensure that the bookmark endpoint functions correctly,
    So that I can manage my bookmarks effectively.

    Background:
        Given I navigate to the Finding The Truth application

    Scenario: Landing page loads and displays correct content
        Then landing page is displayed containing header text "FINDING THE TRUTH"
        And image section is visible
        And first paragraph text is "Explore three cases to explore different aspects of the criminal justice system. Are you more likely to side with the establishment, or to sit on the side of the individual?"
        And second paragraph text is "Note - you will need audio in order to get the most out of this game."
        And START button is visible

    Scenario: Clicking START button navigates user to the case selection page
        When I click the START button
        Then I am navigated to the case selection page

