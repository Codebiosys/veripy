import time
import logging
from behave import when
from veripy.pages import Page
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


@when('the browser is at "{page_name}" after {seconds:d} second{plural:optional_plural}')
def when_wait_page_switch(context, page_name, seconds, plural):
    """ Allow the user to specify that the browser has implicitly navigated
    to a new page (usually by clicking a link or submitting a form).
    ::

        When the browser is at "Requisition Detail Page" after 2 seconds

    This step simply changes the context of the browser page to allow the user
    to specify elements using the page's convenience selectors.

    If time doesn't matter, use the following:
    ::

        When the browser is now at "Requisitions Page"

    This statement not only switches the context, but asserts that the current URL
    is correct for the given page context.
    """
    logger.info(f'Switching page context to "{page_name}" after {seconds} seconds')
    time.sleep(seconds)
    context.page = Page(page_name, context.browser)
