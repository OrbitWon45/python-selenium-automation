from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ProductsPage(Page):
    NOVISON_5_PACK_READING_GLASSES = (By.CSS_SELECTOR, '[alt*="NOVIVON 5 Pack Reading Glasses Men Blue Light Blocking, Lightweight Half Frame Metal Readers with Spring Hinges"]')

    def click_on_glasses(self):
        self.wait_for_element_clickable_click(*self.NOVISON_5_PACK_READING_GLASSES)

    def open_amazon_product(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')
        sleep(2)

