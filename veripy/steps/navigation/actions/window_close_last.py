import logging
from behave import when

logger = logging.getLogger('navigation')


# New
@when('the last opened {screen_type} is closed')
# Old
@when('the user closes the last opened {screen_type}')
def window_close_last(context, screen_type):
    """ Tells the browser to close was most recently openened
    ::

        When the last opened tab is closed

    """

    if screen_type not in ('window', 'tab'):
        raise Exception('Must specify either window or tab')

    context.browser.windows.current = context.browser.windows[0]
    context.browser.windows[-1].close()
