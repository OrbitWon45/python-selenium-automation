from behave import given, when, then


@then('Verify Blog is opened')
def verify_opened(context):
    context.app.blog_page.verify_opened()


@then('close blog')
def close_page(context):
    context.app.blog_page.close_page()


@then('return to original window')
def return_to_original_window(context):
    context.app.blog_page.return_to_original_window(context.original_window)
