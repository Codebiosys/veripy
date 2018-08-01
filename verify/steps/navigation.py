from behave import when, given

from pages import Page


@given('that the browser is at "{name}"')
def browser_is_at(context, name):
    """ Tells the browser to load a specific page designated by an identifer.

    In order to interact with a page, you must first perform this check. This
    statement sets the page context so that later steps can refer to the page
    by it's predefined identifiers.
    """
    context.page = Page(name, context.browser)
    context.page.browser.visit(context.page.url)


@when('the user waits {seconds:d} seconds for the {element_name} to be visible')
def wait_for_element(context, seconds, element_name):
    """ Wait for a given element on the page to become visible. """
    context.page.wait_for(element_name, wait_time=seconds)
