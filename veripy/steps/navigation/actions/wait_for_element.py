import logging
from behave import when, given

logger = logging.getLogger('navigation')


@given('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
@when('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
def when_wait_for_element(context, seconds, element_name):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    logger.info(f'Waiting {seconds} for "{element_name}" to be visible.')
    context.page.wait_for(element_name, wait_time=seconds)
