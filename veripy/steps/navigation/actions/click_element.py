import logging
from behave import given, when

logger = logging.getLogger('navigation')


@given('the user clicks the "{element_name}"')
@when('the user clicks the "{element_name}"')
def when_click_element(context, element_name):
    """ Tells the browser to click on an element with the given identifier.
    ::

        When the user clicks the "Search Button"
    """
    logger.info(f'Clicking on element: "{element_name}".')
    try:
        element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The {element_name} was not found on the page')

    element.click()
