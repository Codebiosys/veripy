import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element_name}" has the value "{text}"')
def check_input_value(context, element_name, text):

    """ Asserts that a form element has the given value.
    This is useful in identifying the value of a given field.

    - Users can assert that a field has a value.

    ::

        The "Phone Number Field" has the value "123-123-1231"
    """
    logger.info(f'Asserting that the element "{element_name}" has the value "{text}".')

    try:
        page_element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    try:
        element_value = page_element.value
    except KeyError:
        raise AssertionError(
            f'The "{element_name}" does not have a value, '
            f'and may not be a form input.'
        )

    assert text == element_value, (
        f'The "{element_name}" was supposed have the value "{text}", '
        'but instead had the value "{element_value}".'
    )
