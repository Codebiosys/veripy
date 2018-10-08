import logging
from behave import when

logger = logging.getLogger('navigation')


@when('the user closes the last opened {screen}')
def window_close_last(context, screen):
    """ Tells the browser to close was most recently openened
    ::

        When the use closes the last opened tab
    """

    if screen not in ('window', 'tab'):
        raise Exception('Must specify either window or tab')

    context.browser.windows.current = context.browser.windows[0]
    context.browser.windows[-1].close()
