import logging
from behave import then

logger = logging.getLogger('content')


def visibility_check(context, element_name, not_):
    logger.info(f'Asserting that the element "{element_name}" is {"not " if not_ else ""}visible.')

    if not_:
        try:
            assert not context.page[element_name].visible, (
                f'The "{element_name}" was not supposed to be visible but it was.'
            )
        except context.page.ElementNotFound:
            pass  # Element was not supposed to be found
    else:
        try:
            assert context.page[element_name].visible, (
                f'The "{element_name}" was supposed to be visible but it was not.'
            )
        except context.page.ElementNotFound:
            raise AssertionError(
                f'The "{element_name}" was supposed to be visible but it was not present.'
            )


@then('the following {colname} are {not_:optional_not}visible')
def check_elements_visible(context, colname, not_):
    """ Asserts that the element is the visible on the page.
    """
    if getattr(context, 'table') is None:
        raise AssertionError('No items were defined.')
    if not context.table.has_column(colname):
        raise AssertionError(f'The table does not have a header \'{colname}\'.')

    messages = ''

    for row in context.table:
        try:
            visibility_check(context, row[colname], not_)
        except AssertionError as e:
            for msg in e.args:
                messages += f'{msg}\n'
    if messages:
        raise AssertionError(messages)


@then('the "{element_name}" is {not_:optional_not}visible')
def check_element_visible(context, element_name, not_):
    """ Asserts that the element is the visible on the page.

    ::

        Then the "Modal Window" is not visible

    """
    visibility_check(context, element_name, not_)
