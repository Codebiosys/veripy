import logging
import splinter.exceptions
from behave import when

logger = logging.getLogger('forms')


@when('"{value}" is selected for "{name}"')
def select_option_by(context, value, name):
    """ Tells the browser to select the HTML `<option>` with the specified value.

    ::

        When "MOBILE" is selected for "Contact Options"
    """
    try:
        element = context.page[name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{name}" was not found on the page.')

    try:
        element.select(value)
    except (AttributeError, IndexError, splinter.exceptions.ElementDoesNotExist):
        raise AssertionError(f'"{name}" has no option with value "{value}".')
