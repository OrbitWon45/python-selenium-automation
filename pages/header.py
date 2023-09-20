from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page



class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BNT = (By.ID, 'nav-search-submit-button')
    CLICK_ORDERS = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR,
                  '#nav-signin-tooltip .nav-action-signin-button')
    CLICK_CART = (By.ID, 'nav-cart')
    LANG_SELECT = (By.CSS_SELECTOR, '.icp-nav-flag')
    SPANISH_OPTION = (By.CSS_SELECTOR,
                      'div#nav-flyout-icp a[href="#switch-lang=en_US"]')
    DEPARMENT_SELECTION = (By.ID, 'searchDropdownBox')
    SUBHEADER_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUB_STR}"]')
    NEW_ARRIVALS_SELECT = (By.CSS_SELECTOR, 'div#nav-progressive-subnav a[aria-label*="New Arrivals"]')
    DROP_DOWN_MENS_IMG = (By.CSS_SELECTOR, 'img[src*="SUBNAV/M._CB1648157817_.jpg"]')


    def _get_subheader_dept_locator(self, dept):
        return [self.SUBHEADER_DEPARTMENT[0], self.SUBHEADER_DEPARTMENT[1].replace("{SUB_STR}", dept)]



    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_for_element_clickable_click(*self.SEARCH_BNT)


    def hover_language(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECT)
        actions.move_to_element(lang)
        actions.perform()


    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_SELECT)
        actions.move_to_element(new_arrivals)
        actions.perform()


    def click_orders(self):
        self.click(*self.CLICK_ORDERS)

    def select_department(self, dept):
        department_select = self.find_element(*self.DEPARMENT_SELECTION)
        select = Select(department_select)
        select.select_by_value(f"search-alias={dept}")


    def click_cart_on_amazon(self):
        self.wait_for_element_clickable_click(*self.CLICK_CART)


    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)

    def verify_signin_btn_is_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)


    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGNIN_BTN)

    def verify_spanish_option_present(self):
        self.wait_for_element_to_appear(*self.SPANISH_OPTION)


    def verify_department_selected(self, dept):
        subheader_locator = self._get_subheader_dept_locator(dept)
        self.wait_for_element_to_appear(*subheader_locator)

    def verify_user_sees_dropdown(self):
        self.wait_for_element_to_appear(*self.DROP_DOWN_MENS_IMG)

