# Created by white at 8/11/2023
Feature: Amazon tests

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened


  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opened


  Scenario: Amazon user sees signin button disappears
    Given Open Amazon page
    When Verify Signin btn is clickable
    When Wait for 6 seconds
    Then Verify Signin btn disappears


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And Switch back to original window


  Scenario: Verify that clicking a empty cart tells you 'Your Amazon Cart is empty'
    Given Open Amazon page
    When Click cart
    Then Verify cart is empty


  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 35 links


  Scenario: User can see language options
    Given Open Amazon Page
    When Hover over language options
    Then Verify Spanish option present









