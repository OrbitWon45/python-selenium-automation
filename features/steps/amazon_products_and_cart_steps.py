from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

NOVISON_5_PACK_READING_GLASSES = (By.CSS_SELECTOR, 'img[alt*="NOVIVON 5 Pack Reading Glasses Men Blue Light Blocking, Lightweight Half Frame Metal Readers with Spring Hi..."]')
CLICK_ADD_TO_CART = (By.ID, "add-to-cart-button")
NOVISON_5_PACK_READING_GLASSES_TEXT = (By.CSS_SELECTOR, 'a.a-link-normal.sc-product-link span.a-truncate-cut')


@when('pick a pair of glasses')
def pick_a_pair_of_glasses(context):
    context.driver.find_element(*NOVISON_5_PACK_READING_GLASSES).click()


@when('add product to cart')
def add_product_to_cart(context):
    context.driver.find_element(*CLICK_ADD_TO_CART).click()


@then('verify glasses are added to cart')
def verify_glasses_are_added_to_cart(context):
    expected_result = 'NOVIVON 5 Pack Reading Glasses for Men'
    actual_result = context.driver.find_element(*NOVISON_5_PACK_READING_GLASSES_TEXT).text
    assert expected_result[:30] == actual_result[:30], f'expected product {expected_result[:30]} does not match actual product {actual_result[:30]}'
    print('test case passed!')