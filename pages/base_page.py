from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        windows = self.driver.window_handles
        print(windows)
        return windows

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(all_windows)
        print(f'switching to {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def return_to_original_window(self, window_id):
        print(f'switching to {window_id}')
        self.driver.switch_to.window(window_id)


    def close_page(self):
        self.driver.close()


    def wait_for_element_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
             message=f'element not clickable: {locator}')


    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator),
             message=f'element not clickable: {locator}')
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element_located(locator),
                        message=f'element did not disappear: {locator}')


    def wait_for_element_to_appear(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
                        message=f'element did not appear: {locator}')



    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, partial expected {expected_text} not in actual {actual_text}.'

    def verify_partial_url(self, expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))