from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('Click Orders')
def click_orders_on_amazon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()
    sleep(4)

@then('Verify sign in page opened')
def Verify_sign_in_page_opened_on_amazon(context):
    expected_result = 'Sign in'

    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

    context.driver.find_element(By.ID, 'ap_email')

    print('Test case passed!')


@when('Click cart')
def Click_cart_on_amazon(context):

    context.driver.find_element(By.ID, 'nav-cart').click()
    sleep(4)


@then('Verify cart is empty')
def Verify_cart_is_empty_on_amazon(context):

    expected_result = 'Your Amazon Cart is empty'

    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text

    assert expected_result == actual_result, f'expected {expected_result} not the same as {actual_result}'

    print('test case passed!')