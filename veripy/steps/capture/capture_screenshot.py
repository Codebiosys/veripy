import logging
from behave import then
from veripy.utils.browsers import screenshot_bytes
from selenium.common.exceptions import UnexpectedAlertPresentException

logger = logging.getLogger('capture')


@then('take a screen shot')
def capture_screenshot(context):
    """ Have the browser take a screenshot of the current window. """
    logger.info('Taking a screenshot.')
    try:
        context.step.screenshots.append(screenshot_bytes(context))
    except UnexpectedAlertPresentException:
        raise AssertionError(f'Capturing a screenshot of a browser alert is not supported.')
