from selenium.webdriver.common.by import By
from pages.base_page import Page



class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BNT = (By.ID, 'nav-search-submit-button')
    CLICK_ORDERS = (By.ID, 'nav-orders')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BNT)


    def click_orders(self):
        self.click(*self.CLICK_ORDERS)