import logging
from behave import then

logger = logging.getLogger('content')


def assert_element_text(context, element_name, not_, text):
    """ Asserts that the element contains the given value as text. """
    logger.info(f'Asserting that the element "{element_name}" contains the text "{text}".')

    try:
        page_element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    assert text in page_element.text, (
        f'The "{element_name}" was supposed to contain "{text}", '
        f'but instead had "{page_element.text}".'
    )


@then('the following {colname} are {not_:optional_not}displayed')
def check_elements_have_text(context, colname, not_):
    """ Asserts that the element is the visible on the page.
    """
    if getattr(context, 'table') is None:
        raise AssertionError('No items were defined.')
    if not context.table.has_column('element'):
        raise AssertionError(f'The table does not have a header \'element\'.')

    if not context.table.has_column(colname):
        raise AssertionError(f'The table does not have a header \'{colname}\'.')

    messages = ''

    for row in context.table:
        try:
            assert_element_text(context, row['element'], not_, row[colname])
        except AssertionError as e:
            for msg in e.args:
                messages += f'{msg}\n'
    if messages:
        raise AssertionError(messages)


@then('the "{element_name}" contains the text "{text}"')
def check_element_text(context, element_name, text):
    """ Asserts that the element contains the given value as text. """
    assert_element_text(context, element_name, False, text)


@then('the "{element_name}" does not contain the text "{text}"')
def check_not_element_text(context, element_name, text):
    """ Asserts that the element contains the given value as text. """
    assert_element_text(context, element_name, True, text)
