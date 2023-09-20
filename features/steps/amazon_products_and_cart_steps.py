from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, 'ul.a-unordered-list.a-nostyle.a-button-list li[title]')
CURRENT_COLOR = (By.CSS_SELECTOR, 'div.a-row span.selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.app.products_page.open_amazon_product(product_id)


@when('click on glasses')
def click_on_glasses(context):
    context.app.products_page.click_on_glasses()


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@when('Store product name')
def store_product_name(context):
    context.app.cart_page.store_product_name()



@when('Add product to cart')
def add_product_to_cart(context):
    context.app.cart_page.add_product_to_cart()


@then('Verify glasses are added to cart')
def verify_glasses_are_added_to_cart(context):
    context.app.cart_page.verify_glasses_are_added_to_cart()



@then('Verify user can click through options')
def verify_user_can_click_options(context):
    expected_colors = ['A-4",0.7oz', 'B-4",0.7oz', 'C-5",0.8oz', 'D-5",0.8oz','E-4",0.7oz']
    actual_colors = []
    options = context.driver.find_elements(*COLOR_OPTIONS)
    for color in options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors.append(current_color)
    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('verify cart is empty')
def verify_cart_is_empty_on_amazon(context):
    context.app.cart_page.verify_cart_is_empty_on_amazon()


@then('Verify user sees dropdown')
def verify_user_sees_dropdown(context):
    context.app.header.verify_user_sees_dropdown()

