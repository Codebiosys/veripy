import logging
from behave import then
from veripy import custom_types  # noqa

logger = logging.getLogger('content')


@then('the "{element_name}" checkbox is {not_:optional_not}checked')
def check_checkbox_value(context, element_name, not_):

    """ Asserts that a form checkbox is or is not checked.
    ::

        The "User Accepts Terms" checkbox is checked"
        The "User Accepts Terms" checkbox is not checked"
    """
    logger.info(f'Asserting the checkbox "{element_name}"  checked status.')

    try:
        page_element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" checkbox was not found on the page.')
    try:
        element_checked = page_element.checked
    except KeyError:
        #  NOTE: uncheckable items are always considered 'unchecked', so this
        #  will not happen in most cases.
        raise AssertionError(
            f'The "{element_name}" is not a checkbox.'
        )
    if not_:
        assert not element_checked, (
            f'The "{element_name}" checkbox was not supposed to be checked, '
            'but it was.'
        )
    else:
        assert element_checked, (
            f'The "{element_name}" checkbox was supposed to be checked, '
            'but it was not.'
        )
