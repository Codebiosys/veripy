import logging
import splinter.exceptions
from behave import when

from veripy.exceptions import ImproperlyConfigured

logger = logging.getLogger('forms')


# New
@when('"{value}" is selected for the "{element_name}"')
# Old
@when('"{value}" is selected for "{element_name}"')
def select_option_by(context, value, element_name):
    """ Tells the browser to select the HTML `<option>` with the specified value.

    ::

        When "MOBILE" is selected for the "Contact Options"
    """
    try:
        element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    if element._element.get_attribute('name'):
        # Default to the preferred Splinter select method.
        logger.debug(
            'Select: "{element_name}" has a valid name. Preferring spliter select.'
        )
        try:
            return element.select(value)
        except (AttributeError, IndexError, splinter.exceptions.ElementDoesNotExist):
            raise AssertionError(f'"{element_name}" has no option with value "{value}".')

    # In this case, we haven't got a properly formatted <select> element so
    # we'll attempt to backsolve for its values using XPaths. Splinter
    # makes the assumption that the select element will have a `name` attribute
    # which is unfortunately not a sound assumption. In this case, we just elect
    # to get all of the options that are children of the select w/o caring about
    # how the select is constructed.
    #
    # Note that this method only works if the element was selected by XPath.
    logger.debug(
        'Select: "{element_name}" has no name attribute. Trying XPath reversal select method.'
    )

    properties = context.page.get_element_properties(element_name)
    by = properties.get('by')

    if by != 'xpath':
        raise ImproperlyConfigured(
            f'Cannot select option for select with name "{element_name}". '
            f'It looks like this element was found using "{by}". '
            f'Currently only XPaths are supported for this method.'
        )

    selector = properties['selector']

    try:
        element.find_by_xpath(
            f'{selector}//option[@value="{value}"]'
        )._element.click()
    except (AttributeError, IndexError, splinter.exceptions.ElementDoesNotExist):
        raise AssertionError(f'"{element_name}" has no option with value "{value}".')
