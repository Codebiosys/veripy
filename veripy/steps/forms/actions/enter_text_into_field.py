import logging
import selenium.common.exceptions
from behave import given, when

logger = logging.getLogger('forms')


@given('"{text}" is entered into the "{element_name}"')
@when('"{text}" is entered into the "{element_name}"')
def when_enter_text_into_input(context, text, element_name):
    """ Tells the browser to enter the given test into an element with
    the given identifier.

    ::

        Given "query text" is entered into the "Search Box"
        # or
        When "query text" is entered into the "Search Box"

    """
    logger.info(f'Entering text: "{text}" into selector "{element_name}".')
    try:
        input = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')
    try:
        input.fill(text)
    except selenium.common.exceptions.InvalidElementStateException:
        raise AssertionError(f'The "{element_name}" cannot accept text.')
