from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    CLICK_ADD_TO_CART = (By.ID, "add-to-cart-button")
    NOVISON_5_PACK_READING_GLASSES_TEXT = (By.CSS_SELECTOR, '.a-truncate.sc-grid-item-product-title.a-size-base-plus')
    PRODUCT_NAME = (By.ID, 'productTitle')

    def verify_cart_is_empty_on_amazon(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART_TEXT)

    def add_product_to_cart(self):
        self.wait_for_element_clickable_click(*self.CLICK_ADD_TO_CART)

    def store_product_name(self):
        self.product_name = self.driver.find_element(*self.PRODUCT_NAME).text

    def verify_glasses_are_added_to_cart(self,):
        expected_result = self.product_name
        actual_result = self.driver.find_element(*self.NOVISON_5_PACK_READING_GLASSES_TEXT).text
        assert expected_result[:30] == actual_result[:30], \
            f'expected product {expected_result[:30]} does not match actual product {actual_result[:30]}'
