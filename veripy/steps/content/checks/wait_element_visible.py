import logging
from behave import then
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


# New
@then('the "{element_name}" is visible after {seconds:d} second{plural:optional_plural}')
def then_wait_for_element(context, element_name, seconds, plural):
    """ Wait for a given element on the page to become visible.

    ::

        Then the "Page Title" is visible after 3 seconds

    """
    logger.info(f'Waiting {seconds}, then looking for {element_name}')
    try:
        context.page.wait_for(element_name, wait_time=seconds)
        assert context.page[element_name].visible, (
            f'The "{element_name}" was supposed to be visible but it was not.'
        )
    except context.page.ElementNotFound:
        raise AssertionError(
            f'The "{element_name}" was supposed to be visible but it was not present.'
        )
