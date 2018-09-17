import logging
from behave import when, given
from veripy.pages import Page

logger = logging.getLogger('navigation')


@given('the browser is now at "{name}"')
@when('the browser is now at "{name}"')
def given_when_page_switch(context, name):
    """ Allow the user to specify that the browser has implicitly navigated
    to a new page (usually by clicking a link or submitting a form).
    ::

        When the browser is now at "Requisitions"
        # or
        Given the browser is now at "Requisitions"

    This step simply changes the context of the browser page to allow the user
    to specify elements using the page's convenience selectors.

    In some cases it is not possible to assert that the page URL is some value
    because the value is determined at runtime (dynamic URLs, etc). In most cases
    users should prefer the assertion statement:
    ::

        Then the browser should be at "Requisitions"

    This statement not only switches the context, but asserts that the current URL
    is correct for the given page context.
    """
    logger.info(f'Switching page context to "{name}"')
    context.page = Page(name, context.browser)
