import logging
from behave import given

from veripy.pages import Page

logger = logging.getLogger('navigation')


@given('that the browser is at "{name}"')
def given_browser_is_at(context, name):
    """ Tells the browser to load a specific page designated by an identifer.
    ::

        Given that the browser is at "google.com"

    In order to interact with a page, you must first perform this check. This
    statement sets the page context so that later steps can refer to the page
    by it's predefined identifiers.
    """
    logger.info(f'Navigating to page named "{name}"')
    context.page = Page(name, context.browser)
    context.page.browser.visit(context.page.url)
