import time
import logging
from behave import then
from veripy.pages import Page
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


# New
@then('after {seconds:d} second{plural:optional_plural}, the browser is at "{page_name}"')
def then_wait_page_switch(context, seconds, plural, page_name):
    """ Assert that the browser has navigated to the new given page, and switch
    the page context to the new page.
    ::

        Then after 3 seconds, the browser is at "Requisitions Page"

    This step simply changes the context of the browser page to allow the user
    to specify elements using the page's convenience selectors.

    If the user has implicitly landed on a page (as a result of a button click,
    or form submission) that has a dynamic URL, asserting the page URL will cause
    a failure. In those cases, use the following variation.
    ::

        When the browser is now at "Requisitions Page"
        # or
        Given the browser is now at "Requisitions Page"

    These variations do the same context switch without asserting the current URL
    is the same as the page URL value.
    """
    logger.info(
        f'After {seconds} seconds, asserting the page is "{page_name}" and switching contexts.'
    )
    page = Page(page_name, context.browser)

    time.sleep(seconds)
    assert page.url == context.browser.url, (
        f'Expected to be on the Page "{page_name}", but was not.'
    )
    context.page = page
