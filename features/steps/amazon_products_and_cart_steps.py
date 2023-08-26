from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

NOVISON_5_PACK_READING_GLASSES = (By.CSS_SELECTOR, 'img[alt*="NOVIVON 5 Pack Reading Glasses Men Blue Light Blocking, Lightweight Half Frame Metal Readers with Spring Hi..."]')
CLICK_ADD_TO_CART = (By.ID, "add-to-cart-button")
PRODUCT_NAME = (By.ID, 'productTitle')
NOVISON_5_PACK_READING_GLASSES_TEXT = (By.CSS_SELECTOR, '.a-truncate.sc-grid-item-product-title.a-size-base-plus')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'ul.a-unordered-list.a-nostyle.a-button-list li[title]')
CURRENT_COLOR = (By.CSS_SELECTOR, 'div.a-row span.selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Pick a pair of glasses')
def pick_a_pair_of_glasses(context):
    context.driver.wait.until(EC.element_to_be_clickable(NOVISON_5_PACK_READING_GLASSES)).click()


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text



@when('Add product to cart')
def add_product_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CLICK_ADD_TO_CART)).click()


@then('Verify glasses are added to cart')
def verify_glasses_are_added_to_cart(context):
    expected_result = context.product_name
    actual_result = context.driver.find_element(*NOVISON_5_PACK_READING_GLASSES_TEXT).text
    assert expected_result[:30] == actual_result[:30],\
        f'expected product {expected_result[:30]} does not match actual product {actual_result[:30]}'



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

