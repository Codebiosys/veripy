from behave import then


@then('the page title should be "{title}"')
def check_page_title(context, title):
    """ Asserts that the browser page's current title is the given value. """
    assert context.page.browser.title == title


@then('the "{element}" contains the text "{text}"')
def check_element_text(context, element, text):
    """ Asserts that the element contains the given value as text. """
    assert text in context.page[element].text


@then('the "{element}" is {not_:optional_not}visible')
def check_element_visible(context, element, not_):
    """ Asserts that the element is the visible on the page. """
    try:
        assert context.page[element].visible != not_
    except AttributeError:
        assert not_
