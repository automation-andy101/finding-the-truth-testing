Feature: Case One User Journeys

    As a Finding the Truth user I want to explorer different user journeys after selecting case one
    so that I can learn more about the case

    Background:
        Given I have selected case one

    Scenario: Case selection page loads and displays correct content
        Given I click the JUDGE THIS button under the video
        When I select the Guilt radio button
        And click the VOTE button
        Then a popup modals stating "GUILTY!"
