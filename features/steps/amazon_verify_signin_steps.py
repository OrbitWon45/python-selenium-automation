from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

EMAIL_FIELD = (By.ID, 'ap_email')


@then('Verify sign in page opened')
def Verify_sign_in_page_opened_on_amazon(context):
    expected_result = 'Sign in'

    actual_result = context.driver.find_element(*SIGNIN_TEXT).text

    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

    context.driver.find_element(*EMAIL_FIELD)

    print('test case passed!')