import logging
from behave import when
from veripy import custom_types  # noqa
from selenium.common.exceptions import NoAlertPresentException

logger = logging.getLogger('navigation')


@when('the browser prompt is {action:prompt_action}')
def when_prompted(context, action):
    """ Interact with a prompt by either pressing the confirm or cancel button.
    ::

        When the browser prompt is cancelled

    """
    logger.info(f'the browser prompt will be {action}')
    try:
        alert = context.browser.driver.switch_to_alert()
        if action in ['accepted', 'confirmed']:
            alert.accept()
        else:
            alert.dismiss()
    except NoAlertPresentException:
        raise AssertionError(f'The browser prompt was not available, and could not be {action}.')
