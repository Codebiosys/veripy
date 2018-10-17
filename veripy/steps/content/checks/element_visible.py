import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element_name}" is {not_:optional_not}visible')
def check_element_visible(context, element_name, not_):
    """ Asserts that the element is the visible on the page.

    ::

        Then the "Modal Window" is not visible

    """
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
