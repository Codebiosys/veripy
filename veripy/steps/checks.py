from behave import then


@then('the page title should be "{title}"')
def check_page_title(context, title):
    """ Asserts that the browser page's current title is the given value. """
    assert context.page.browser.title == title
