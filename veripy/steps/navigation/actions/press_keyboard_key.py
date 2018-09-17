import logging
from behave import when
from veripy import custom_types  # noqa

logger = logging.getLogger('navigation')


@when('the user presses the "{keyboard_key:pressable_key_type}" key')
def when_press_key(context, keyboard_key):
    """ Press the given key.
    ::

        the user presses the "Return" key
    """
    logger.info(f'Pressing the "{keyboard_key}" key.')
    active_web_element = context.browser.driver.switch_to.active_element
    active_web_element.send_keys(keyboard_key)
