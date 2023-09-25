from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class BestSellersPage(Page):

    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


    def open_amazon_bestsellers(self):
        self.open_url('gp/bestsellers/')
        sleep(2)
        self.driver.refresh()


    def click_thr_top_links(self):
        top_links = self.find_elements(*self.TOP_LINKS)
        for i in range(len(top_links)):
            link_to_click = self.find_elements(*self.TOP_LINKS)[i]
            link_text = link_to_click.text
            link_to_click.click()
            sleep(1)
            self.verify_partial_text(link_text, *self.HEADER)

    def verify_links_are_present(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.driver.find_elements(*self.TOP_LINKS)
        assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
