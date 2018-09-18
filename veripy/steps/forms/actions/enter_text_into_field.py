import logging
import selenium.common.exceptions
from behave import given, when

logger = logging.getLogger('forms')


@given('"{text}" is entered into the "{input_name}"')
@when('"{text}" is entered into the "{input_name}"')
def when_enter_text_into_input(context, text, input_name):
    """ Tells the browser to enter the given test into an element with
    the given identifier.
    ::

        When "query text" is entered into the "Search Box"

    """
    logger.info(f'Entering text: "{text}" into selector "{input_name}".')
    try:
        input = context.page[input_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{input_name}" was not found on the page.')
    try:
        input.fill(text)
    except selenium.common.exceptions.InvalidElementStateException:
        raise AssertionError(f'The "{input_name}" cannot accept text.')
