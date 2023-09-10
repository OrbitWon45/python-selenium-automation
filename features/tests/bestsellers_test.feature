# Created by white at 9/8/2023
Feature: BestSellers

  Scenario: Top links can be opened
    Given Open Amazon Bestsellers
    Then User can click thr top links


  Scenario: Verify 5 links on Best Sellers page
    Given Open Amazon Bestsellers
    Then Verify 5 links are present