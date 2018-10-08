import logging
from behave import when

logger = logging.getLogger('navigation')


@when('the user switches to the last opened {screen}')
def window_focus_last(context, screen):
    """ Tells the browser to switch to the tab that was most recently openened
    ::

        When the use switches to the last opened tab
    """

    if screen not in ('window', 'tab'):
        raise Exception('Must specify either window or tab')

    context.browser.windows.current = context.browser.windows[-1]
