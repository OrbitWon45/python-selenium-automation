from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




LINKS = (By.CSS_SELECTOR, '#zg_header a')



@given('open amazon bestsellers')
def open_amazon_bestsellers(context):
    context.app.bestsellers_page.open_amazon_bestsellers()


@then('verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@then('verify {expected_amount} links are present')
def verify_links_are_present(context, expected_amount):
    context.app.bestsellers_page.verify_links_are_present(expected_amount)


@then('user can click thr top links')
def click_thr_top_links(context):
    context.app.bestsellers_page.click_thr_top_links()


@then('Verify {dept} department is selected')
def verify_department_selected(context, dept):
    context.app.header.verify_department_selected(dept)
