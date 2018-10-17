import logging
import splinter.exceptions
from behave import when

logger = logging.getLogger('forms')


# New
@when('"{value}" is selected for the "{element_name}"')
# Old
@when('"{value}" is selected for "{element_name}"')
def select_option_by(context, value, element_name):
    """ Tells the browser to select the HTML `<option>` with the specified value.

    ::

        When "MOBILE" is selected for the "Contact Options"
    """
    try:
        element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    try:
        element.select(value)
    except (AttributeError, IndexError, splinter.exceptions.ElementDoesNotExist):
        raise AssertionError(f'"{element_name}" has no option with value "{value}".')
