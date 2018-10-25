import logging
import selenium.common.exceptions
from behave import given, when

logger = logging.getLogger('forms')


def enter_text_into_input(context, text, element_name):
    """
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


@given('the following {colname} are entered')
@when('the following {colname} are entered')
def when_text_into_inputs(context, colname):
    """ Asserts that the element is the visible on the page.
    """
    if getattr(context, 'table') is None:
        raise AssertionError('No items were defined.')
    if not context.table.has_column('field'):
        raise AssertionError(f'The table does not have a header \'field\'.')
    if not context.table.has_column(colname):
        raise AssertionError(f'The table does not have a header \'{colname}\'.')

    messages = ''

    for row in context.table:
        try:
            enter_text_into_input(context, row[colname], row['field'])
        except AssertionError as e:
            for msg in e.args:
                messages += f'{msg}\n'
    if messages:
        raise AssertionError(messages)


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
    enter_text_into_input(context, text, element_name)
