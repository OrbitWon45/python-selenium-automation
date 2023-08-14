# Created by white at 8/11/2023
Feature: Amazon tests

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
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


  Scenario: Verify that you can add a product to the cart
    Given Open Amazon page
    When Search for NOVIVON 5 Pack Reading Glasses for Men
    When Pick a pair of glasses
    When add product to cart
    When click cart
    Then Verify glasses are added to cart


    Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_product>
    Then Verify search result is <search_result>
    Examples:
    |search_product  |search_result |
    |table           |"table"       |
    |flowers         |"flowers"     |
