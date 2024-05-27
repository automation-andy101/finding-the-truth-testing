Feature: [UI TEST] Case One User Journeys

    As a Finding the Truth user I want to explorer different user journeys after selecting case one
    so that I can learn more about the case

    Background:
        Given I have selected case one

    Scenario: Case selection page loads and displays correct content
        Given I click the JUDGE THIS button under the video
        When I select the Guilty radio button
        And click the VOTE button
        Then popup modal appears stating "GUILTY!"
