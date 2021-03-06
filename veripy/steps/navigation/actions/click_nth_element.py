import logging
import splinter.exceptions
import selenium.common.exceptions

from behave import when, given
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


# New
@given('the {position:d}{ordinal:ordinal_indicator} option in the "{elements_name}" is clicked')
@when('the {position:d}{ordinal:ordinal_indicator} option in the "{elements_name}" is clicked')
# Old
@given(
    'the user clicks on the {position:d}{ordinal:ordinal_indicator} option '
    'in the "{elements_name}"'
)
@when(
    'the user clicks on the {position:d}{ordinal:ordinal_indicator} option '
    'in the "{elements_name}"'
)
def when_click_nth_element(context, position, ordinal, elements_name):
    """ Tells the browser to click on the nth option in the list of elements of the given identifier.

    ::

        Given the 2nd option in the "Table Rows" is clicked
        # Or
        When the 2nd option in the "Table Rows" is clicked

    Note that in order for this step to work properly, you *must* specify
    ``allow_multiple`` to ``true`` in the page fixture.
    """
    logger.info(f'Clicking on {position}{ordinal} option the element: "{elements_name}".')

    try:
        elements = context.page[elements_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{elements_name}" was not found on the page.')

    try:
        nth_element = elements[position - 1]
    except (IndexError, splinter.exceptions.ElementDoesNotExist):
        raise AssertionError(
            f'The "{elements_name}" does not have a {position}{ordinal} option.'
            )

    try:
        nth_element.click()
    except (AttributeError, selenium.common.exceptions.ElementNotVisibleException):
        raise AssertionError(
            f'The "{elements_name}" does not have a {position}{ordinal} option that is clickable.'  # noqa: E501
            )
