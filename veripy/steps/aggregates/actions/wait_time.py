import time
import logging
from behave import when, given, then
from veripy import custom_types  # noqa
from veripy.utils.extract_substep_response import extract_substep_response

logger = logging.getLogger('navigation')


def wait_for(context, seconds, sentence):
    """
    """
    logger.info(f'Waiting {seconds}')
    time.sleep(seconds)
    try:
        return context.execute_steps(f'{context.step.step_type} {sentence}')
    except AssertionError as error:
        newMessage = extract_substep_response(error)
        raise AssertionError(newMessage)


@given('after a few seconds, {sentence}')
@when('after a few seconds, {sentence}')
@then('after a few seconds, {sentence}')
def wait_a_few(context, sentence):
    """ Wait for a given element on the page to become visible.
        This is the same as "after 3 seconds, do something", and
        is provided in the common case so that waiting specific amount
        of time isn't considered a requirement
    ::

        Given after a few seconds, the browser is at "Home Page"
        # or
        When after a few seconds, the "Go Button" is clicked

    """
    return wait_for(context, 3, sentence)


@given('after {seconds:d} second{plural:optional_plural}, {sentence}')
@when('after {seconds:d} second{plural:optional_plural}, {sentence}')
@then('after {seconds:d} second{plural:optional_plural}, {sentence}')
def wait_seconds(context, seconds, plural, sentence):
    """ Wait for a given element on the page to become visible.

    ::

        Given after 10 seconds, the browser is at "Home Page"
        # or
        When after 10 seconds, the "Go Button" is clicked

    """
    return wait_for(context, seconds, sentence)
