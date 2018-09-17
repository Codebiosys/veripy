import logging
from behave import when, given

logger = logging.getLogger('navigation')


@given('the user waits {seconds:d} seconds')
@when('the user waits {seconds:d} seconds')
def when_wait(context, seconds):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    logger.info(f'Waiting {seconds}')
    context.page.wait_for('body', wait_time=seconds)
