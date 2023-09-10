from behave import given, when, then

@given('Open Amazon T&C page')
def open_t_and_c_page(context):
    context.app.signin_page.open_t_and_c_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.signin_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.app.signin_page.click_privacy_notice()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.signin_page.switch_to_new_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.app.signin_page.verify_privacy_notice_page_opened()



@then('Verify sign in page opened')
def verify_signin_page_opened(context):
    context.app.signin_page.verify_signin_page_opened()


@then('User can close new window')
def close_page(context):
    context.app.signin_page.close_page()


@then('Switch back to original window')
def return_to_original_window(context):
    context.app.signin_page.return_to_original_window(context.original_window)
