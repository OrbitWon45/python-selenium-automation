from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(Page):
    NOVISON_5_PACK_READING_GLASSES = (By.CSS_SELECTOR, '[alt*="NOVIVON 5 Pack Reading Glasses Men Blue Light Blocking, Lightweight Half Frame Metal Readers with Spring Hinges"]')

    def click_on_glasses(self):
        self.wait_for_element_clickable_click(*self.NOVISON_5_PACK_READING_GLASSES)


