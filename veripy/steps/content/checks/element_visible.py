import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element}" is {not_:optional_not}visible')
def check_element_visible(context, element, not_):
    """ Asserts that the element is the visible on the page. """
    logger.info(f'Asserting that the element "{element}" is {"not " if not_ else ""}visible.')

    if not_:
        try:
            assert not context.page[element].visible, (
                f'The element "{element}" was not supposed to be visible and was.'
            )
        except context.page.ElementNotFound:
            pass  # Element was not supposed to be found
    else:
        try:
            assert context.page[element].visible, (
                f'The element "{element}" was supposed to be visible and was not.'
            )
        except context.page.ElementNotFound:
            raise AssertionError(f'The element "{element}" was supposed to be visible and was not.')
