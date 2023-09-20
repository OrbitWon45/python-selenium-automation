from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep




FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')


@given('open amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main()

@when('wait for 6 seconds')
def wait_for_seconds(context):
    sleep(6)


@when('Hover over language options')
def hover_language(context):
    context.app.header.hover_language()

@when('Search for {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)


@when('Select department by alias {dept}')
def select_department(context, dept):
    context.app.header.select_department(dept)


@when('click Orders')
def click_orders_on_amazon(context):
    context.app.header.click_orders()



@when('click cart')
def click_cart_on_amazon(context):
    context.app.header.click_cart_on_amazon()


@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.app.header.click_signin_from_popup()


@when('verify signin btn is clickable')
def verify_signin_btn_is_clickable(context):
    context.app.header.verify_signin_btn_is_clickable()


@then('verify signin btn disappears')
def verify_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappears()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount,\
        f'Expected {expected_amount} links but got {len(links)}'


@then('Verify Spanish option present')
def verify_spanish_option_present(context):
    context.app.header.verify_spanish_option_present()



