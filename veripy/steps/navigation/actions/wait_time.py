import logging
from behave import when, given

logger = logging.getLogger('navigation')


@given('the user waits {seconds:d} second{plural}')
@when('the user waits {seconds:d} second{plural}')
def when_wait(context, seconds, plural):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    logger.info(f'Waiting {seconds}')
    context.browser.is_element_present_by_tag('body', wait_time=seconds)
