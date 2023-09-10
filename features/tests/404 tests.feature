# Created by white at 9/8/2023
Feature: 404 tests

  Scenario: User is able to navigate to Blog from 404 page
    Given Open Amazon product B07NF5WGQ11111111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify Blog is opened
    And Close Blog
    And Return to original window