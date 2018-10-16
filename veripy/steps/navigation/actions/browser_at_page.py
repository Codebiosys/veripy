import logging
from behave import given

from veripy.pages import Page

logger = logging.getLogger('navigation')


# New
@given('the browser is at "{page_name}"')
# Old
@given('that the browser is at "{page_name}"')
def given_browser_is_at(context, page_name):
    """ Tells the browser to load a specific page designated by an identifer.
    ::

        Given the browser is at "Google Home Page"

    In order to interact with a page, you must first perform this check. This
    statement sets the page context so that later steps can refer to the page
    by it's predefined identifiers.
    """
    logger.info(f'Navigating to page named "{page_name}"')
    context.page = Page(page_name, context.browser)
    context.page.browser.visit(context.page.url)
