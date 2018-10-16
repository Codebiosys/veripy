import logging
from behave import then

logger = logging.getLogger('content')


@then('the "{element_name}" contains the text "{text}"')
def check_element_text(context, element_name, text):
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
