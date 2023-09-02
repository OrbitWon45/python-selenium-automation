from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




LINKS = (By.CSS_SELECTOR, '#zg_header a')



@given('open best sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@then('verify {expected_amount} links are present')
def verify_5_links_are_present(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*LINKS)
    assert  len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
