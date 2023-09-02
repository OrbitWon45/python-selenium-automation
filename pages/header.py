from selenium.webdriver.common.by import By
from pages.base_page import Page



class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BNT = (By.ID, 'nav-search-submit-button')
    CLICK_ORDERS = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR,
                  '#nav-signin-tooltip .nav-action-signin-button')
    CLICK_CART = (By.ID, 'nav-cart')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_for_element_clickable_click(*self.SEARCH_BNT)

    def click_orders(self):
        self.click(*self.CLICK_ORDERS)

    def click_cart_on_amazon(self):
        self.wait_for_element_clickable_click(*self.CLICK_CART)


    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)

    def verify_signin_btn_is_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)


    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGNIN_BTN)
