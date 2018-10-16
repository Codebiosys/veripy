import logging
import splinter.exceptions
from behave import then

logger = logging.getLogger('content')


# New
@then(
    'the {position:d}{ordinal:ordinal_indicator} item in the "{element_name}" '
    'contains the text "{text}"'
)
# Old
@then(
    'the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" '
    'contains the text "{text}"'
)
def check_nth_element_text(context, position, ordinal, element_name, text, words='item'):
    """ Asserts that the nth element contains the given value as text
    ::

        Then the 3rd item in the "Form Labels" contains the text "First Name"

    Note: in order to for this step to function properly, ``{"kwargs": "allow_mulitple": true}``
    must be set for the element definition in the page fixture.
    """
    logger.info(
        f'Asserting that the {position}{ordinal} "{words}" of the element: '
        f'"{element_name}" contains the text "{text}".'
    )

    try:
        page_element = context.page[element_name]

    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')
    try:
        nth_element = page_element[position-1]
    except (IndexError, splinter.exceptions.ElementDoesNotExist):
        raise AssertionError(
            f'The "{element_name}" does not have a {position}{ordinal} {words}.'
        )

    assert text in nth_element.text, \
        f'The {position}{ordinal} {words} in the "{element_name}" should have contained the text "{text}", but it did not.'  # noqa: E501
