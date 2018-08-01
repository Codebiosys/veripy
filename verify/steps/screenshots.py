from behave import *

from pages import Page
from utils.browsers import screenshot_bytes


@then('take a screenshot')
def take_screenshot(context):
    """ Have the browser take a screenshot of the current window. """
    context.step.screenshots.append(screenshot_bytes(context))
