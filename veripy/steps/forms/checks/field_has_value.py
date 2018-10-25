import logging
from behave import then

logger = logging.getLogger('content')


def assert_input_value(context, element_name, text):
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
        f'but instead had the value "{element_value}".'
    )


@then('the following fields have the specified values')
def check_input_values(context):
    """ Asserts that the element is the visible on the page.
    """
    if getattr(context, 'table') is None:
        raise AssertionError('No items were defined.')
    if not context.table.has_column('field'):
        raise AssertionError(f'The table does not have a header \'field\'.')
    if not context.table.has_column('value'):
        raise AssertionError(f'The table does not have a header \'value\'.')

    messages = ''

    for row in context.table:
        try:
            assert_input_value(context, row['field'], row['value'])
        except AssertionError as e:
            for msg in e.args:
                messages += f'{msg}\n'
    if messages:
        raise AssertionError(messages)


@then('the "{element_name}" has the value "{text}"')
def check_input_value(context, element_name, text):

    """ Asserts that a form element has the given value.
    This is useful in identifying the value of a given field.

    - Users can assert that a field has a value.

    ::

        The "Phone Number Field" has the value "123-123-1231"
    """
    assert_input_value(context, element_name, text)
