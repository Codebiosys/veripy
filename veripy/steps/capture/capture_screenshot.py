import logging
from behave import then
from veripy.utils.browsers import screenshot_bytes

logger = logging.getLogger('capture')


@then('take a screen shot')
def capture_screenshot(context):
    """ Have the browser take a screenshot of the current window. """
    logger.info('Taking a screenshot.')
    context.step.screenshots.append(screenshot_bytes(context))
