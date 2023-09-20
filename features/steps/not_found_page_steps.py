from behave import given, when, then


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.not_found_page.get_current_window()


@when('click on a dog image')
def click_dog_img(context):
    context.app.not_found_page.click_dog_img()


@when('switch to new window')
def switch_to_new_window(context):
    context.app.not_found_page.switch_to_new_window()