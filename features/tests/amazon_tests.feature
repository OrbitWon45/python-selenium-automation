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


  Scenario: Verify that clicking a empty cart tells you 'Your Amazon Cart is empty'
    Given Open Amazon page
    When Click cart
    Then Verify cart is empty


  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 35 links


  Scenario: Verify 5 links on Best Sellers page
    Given Open Best Sellers page
    Then Verify 5 links are present






