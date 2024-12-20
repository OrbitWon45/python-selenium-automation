from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.bestsellers_page import BestSellersPage
from pages.not_found_page import NotFoundPage
from pages.blog_page import BlogPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.products_page = ProductsPage(driver)
        self.bestsellers_page = BestSellersPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.blog_page = BlogPage(driver)