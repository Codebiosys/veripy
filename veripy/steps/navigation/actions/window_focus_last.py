import logging
from behave import when

logger = logging.getLogger('navigation')


# New
@when('the last opened {screen_type} is focused')
# Old
@when('the user switches to the last opened {screen_type}')
def window_focus_last(context, screen_type):
    """ Tells the browser to switch to the tab that was most recently openened
    ::

        When the last opened tab is focused
    """

    if screen_type not in ('window', 'tab'):
        raise Exception('Must specify either window or tab')

    context.browser.windows.current = context.browser.windows[-1]
