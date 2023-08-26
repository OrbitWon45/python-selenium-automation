from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_page_opened(self):
        expected_result = 'Sign in'
        actual_result = self.driver.find_element(*self.SIGNIN_TEXT).text
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
        self.driver.find_element(*self.EMAIL_FIELD)