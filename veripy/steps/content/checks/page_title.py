import logging
from behave import then
from veripy.utils import allow_retries

logger = logging.getLogger('content')


@then('the page title should be "{title}"')
@allow_retries(retry_on=(AssertionError,), retries=1)
def check_page_title(context, title):
    """ Asserts that the browser page's current title is the given value. """
    logger.info(f'Asserting that the page title is "{title}".')
    assert context.page.browser.title == title, (
        f'The page title was supposed to be "{title}" but was not.'
    )
