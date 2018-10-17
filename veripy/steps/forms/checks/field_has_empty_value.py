import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element_name}" has an empty value')
def check_input_empty(context, element_name):
    """ Asserts that a form element has an empty value.
    This is useful in identifying fields that do not have default values.

    - Users can specify that a field has an empty value.

    ::

        The "Phone Number" has an empty value
    """

    logger.info(f'Asserting that the element "{element_name}" has an empty value.')

    try:
        page_element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    try:
        element_value = page_element.value
    except KeyError:
        raise AssertionError(
            f'The "{element_name}" does not have a value property, and may not be a form input.'
        )

    assert '' == element_value, (
        f'The "{element_name}" was supposed have no value, '
        f'but instead had the value "{element_value}".'
    )
