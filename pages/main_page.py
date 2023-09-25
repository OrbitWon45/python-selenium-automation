from pages.base_page import Page
from time import sleep
from suport.logging import logger


class MainPage(Page):

    def open_main(self):
        self.open_url()


