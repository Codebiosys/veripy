import logging
from behave import then
from veripy.pages import Page

logger = logging.getLogger('navigation')


# New
@then('the browser is now at "{page_name}"')
# Old
@then('the browser should be at "{page_name}"')
def then_page_switch(context, page_name):
    """ Assert that the browser has navigated to the new given page, and switch
    the page context to the new page.
    ::

        Then the browser is now at "Requisitions Page"

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
    logger.info(f'Asserting the page is "{page_name}" and switching contexts.')
    page = Page(page_name, context.browser)
    assert page.url == context.browser.url, (
        f'Expected to be on the Page "{page_name}", but was not.'
    )
    context.page = page
