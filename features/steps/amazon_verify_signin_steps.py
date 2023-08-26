from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify sign in page opened')
def verify_signin_page_opened(context):
    context.app.signin_page.verify_signin_page_opened()
