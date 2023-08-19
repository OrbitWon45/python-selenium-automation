from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_TEXT_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
LINKS = (By.CSS_SELECTOR, '#zg_header a')



@given('open best sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(2)


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*PRODUCT_TEXT_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    print('test case passed!')


@then('verify cart is empty')
def verify_cart_is_empty_on_amazon(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(*EMPTY_CART_TEXT).text
    assert expected_result == actual_result, f'expected {expected_result} not the same as {actual_result}'
    print('test case passed!')


@then('verify {expected_amount} links are present')
def verify_5_links_are_present(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*LINKS)
    assert  len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
    print('test case passed')