from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BNT = (By.ID, 'nav-search-submit-button')
CLICK_ORDERS = (By.ID, 'nav-orders')
CLICK_CART = (By.ID, 'nav-cart')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)


@when('click Orders')
def click_orders_on_amazon(context):
    context.app.header.click_orders()



@when('click cart')
def click_cart_on_amazon(context):
    context.driver.wait.until(EC.element_to_be_clickable(CLICK_CART)).click()


@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='SignIn btn from popup not clickable'
    ).click()



@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'



