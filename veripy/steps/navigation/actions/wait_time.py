import time
import logging
from behave import when, given
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


# New
@given('after {seconds:d} second{plural:optional_plural}')
@when('after {seconds:d} second{plural:optional_plural}')
# Old
@given('the user waits {seconds:d} second{plural:optional_plural}')
@when('the user waits {seconds:d} second{plural:optional_plural}')
def when_wait(context, seconds, plural):
    """ Wait for a given element on the page to become visible.

    ::

        Given after 10 seconds
        # or
        When after 10 seconds

    """
    logger.info(f'Waiting {seconds}')
    time.sleep(seconds)
    return context.browser.is_element_present_by_tag('body', wait_time=seconds)
