import logging
from behave import then
from veripy.pages import Page

logger = logging.getLogger('navigation')


@then('the browser should be at "{name}"')
def then_page_switch(context, name):
    """ Assert that the browser has navigated to the new given page, and switch
    the page context to the new page.
    ::

        Then the browser should be at "Requisitions"

    This step simply changes the context of the browser page to allow the user
    to specify elements using the page's convenience selectors.

    If the user has implicitly landed on a page (as a result of a button click,
    or form submission) that has a dynamic URL, asserting the page URL will cause
    a failure. In those cases, use the following variation.
    ::

        When the browser is now at "Requisitions"
        # or
        Given the browser is now at "Requisitions"

    These variations do the same context switch without asserting the current URL
    is the same as the page URL value.
    """
    logger.info(f'Asserting the page is "{name}" and switching contexts.')
    page = Page(name, context.browser)
    assert page.url == context.browser.url, f'Expected to be on the Page "{name}", but was not.'
    context.page = page
