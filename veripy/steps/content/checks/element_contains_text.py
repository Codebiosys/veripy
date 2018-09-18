import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element}" contains the text "{text}"')
def check_element_text(context, element, text):
    """ Asserts that the element contains the given value as text. """
    logger.info(f'Asserting that the element "{element}" contains the text "{text}".')

    try:
        page_element = context.page[element]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element}" was not found on the page.')

    assert text in page_element.text, (
        f'The "{element}" was supposed to contain "{text}", but instead had "{page_element.text}".'
    )
