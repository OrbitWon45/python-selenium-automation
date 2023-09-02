from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_page_opened(self):
       self.verify_text('Sign in', *self.SIGNIN_TEXT)
       self.driver.find_element(*self.EMAIL_FIELD)