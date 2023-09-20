from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')
    PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
    PRIVACY_NOTICE_HEADER = (By.CSS_SELECTOR, 'h1#GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64')
    def open_t_and_c_page(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                        'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
                        )
        sleep(2)

    def click_privacy_notice(self):
        self.click(*self.PRIVACY_NOTICE_LINK)


    def verify_privacy_notice_page_opened(self):
        self.verify_text('Amazon.com Privacy Notice',
                         *self.PRIVACY_NOTICE_HEADER
                         )


    def verify_signin_page_opened(self):
       self.verify_text('Sign in', *self.SIGNIN_TEXT)
       self.driver.find_element(*self.EMAIL_FIELD)