# Created by white at 8/18/2023
Feature: Product tests


    Scenario: Verify that you can add a product to the cart
    Given Open Amazon page
    When Search for NOVIVON 5 Pack Reading Glasses for Men
    When Click on glasses
    When Store product name
    When Add product to cart
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


    Scenario: Verify user can click through product options
    Given Open Amazon product B07TRXFY51 page
    Then Verify user can click through options
