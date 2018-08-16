from behave import when, given

from veripy.pages import Page


@given('that the browser is at "{name}"')
def given_browser_is_at(context, name):
    """ Tells the browser to load a specific page designated by an identifer.
    ::

        Given that the browser is at "google.com"

    In order to interact with a page, you must first perform this check. This
    statement sets the page context so that later steps can refer to the page
    by it's predefined identifiers.
    """
    context.page = Page(name, context.browser)
    context.page.browser.visit(context.page.url)


@given('the browser window is {width:d} by {height:d} pixels')
def given_resize_window(context, width, height):
    """ Tells the browser to resize the viewport.
    ::

        Given the browser window is 500 by 1000 pixels

    Resizing the browser viewport will be important for testing the web applciation
    in various device screen sizes such as desktop, phone, tablet, etc.
    """
    # Splinter does not support window resize, so we must do it via driver instead
    # https://stackoverflow.com/a/21062539/148781
    context.page.browser.driver.set_window_size(width, height)


@given('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
@when('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
def when_wait_for_element(context, seconds, element_name):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    context.page.wait_for(element_name, wait_time=seconds)
