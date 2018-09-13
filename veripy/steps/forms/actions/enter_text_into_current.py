import logging
from behave import when

logger = logging.getLogger('forms')


@when('"{text}" is entered into the current field')
def when_enter_text_into_current_input(context, text):
    """ Tells the browser to enter the given test into the element with
    the current focus.
    ::

        When "query text" is entered into the current field

    """
    logger.info(f'Entering text: "{text}" into current element.')
    active_web_element = context.browser.driver.switch_to.active_element
    active_web_element.send_keys(text)
