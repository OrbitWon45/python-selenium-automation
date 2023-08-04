from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path='<provide your absolute path>')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')




# amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# create account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# name field
driver.find_element(By.ID, 'ap_customer_name')

# mobile number or email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# password field
driver.find_element(By.ID, 'ap_password')

# text "password must be at least 6 characters"

# re-enter password field
driver.find_element(By.ID, 'ap_password_check')

# continue button
driver.find_element(By.ID, 'continue')

# conditions of use link
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# privacy link
driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_privacy_notice"]')

# sign in link
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="/ap/signin"]')

