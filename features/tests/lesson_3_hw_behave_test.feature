# Created by white at 8/4/2023
Feature: # Lesson 3 Amazon Behave tests

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened


  Scenario: Verify that clicking a empty cart tells you 'Your Amazon Cart is empty'
    Given Open Amazon page
    When Click cart
    Then Verify cart is empty