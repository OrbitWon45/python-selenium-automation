# Created by white at 8/18/2023
@product
Feature: Product tests

    @smoke
    Scenario: Verify that you can add a product to the cart
        Given Open Amazon page
        When Search for NOVIVON 5 Pack Reading Glasses for Men
        When Click on glasses
        When Store product name
        When Add product to cart
        When click cart
        Then Verify glasses are added to cart

    @smoke
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


    Scenario Outline: User can select and search in a department
        Given Open Amazon page
        When Select department by alias <dept_alias>
        And Search for <search_word>
        Then Verify <dept_selected> department is selected
        Examples:
        |dept_alias     |search_word    |dept_selected   |
        |stripbooks     |Faust          |books           |
        |audible        |Alice in       |audible         |
        |amazon-devices |smart plug     |amazon-devices  |
        
    
    Scenario: Verify user can hover over New Arrivals
        Given Open Amazon product product/B074TBCSC8 page
        When Hover over New Arrivals
        Then Verify user sees dropdown