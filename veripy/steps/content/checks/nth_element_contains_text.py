import logging
from behave import then

logger = logging.getLogger('content')


@then(
    'the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" '
    'contains the text "{text}"'
)
def check_nth_element_text(context, position, ordinal, words, element_name, text):
    """ Asserts that the nth element contains the given value as text
    ::

        the 3rd label of the "Form" contains the text "First Name"
    """
    logger.info(
        f'Asserting that the {position}{ordinal} "{words}" of the element: '
        f'"{element_name}" contains the text "{text}".'
    )

    try:
        page_element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The {element_name} was not found on the page')
    try:
        nth_element = page_element[position-1]
    except IndexError:
        raise AssertionError(f'The {element_name} does not have a {position}{ordinal} {words}')

    assert text in nth_element.text
