import logging
from behave import given

logger = logging.getLogger('navigation')


@given('the browser window is {width:d} by {height:d} pixels')
def given_resize_window(context, width, height):
    """ Tells the browser to resize the viewport.
    ::

        Given the browser window is 500 by 1000 pixels

    Resizing the browser viewport will be important for testing the web applciation
    in various device screen sizes such as desktop, phone, tablet, etc.
    """
    logger.info(f'Resizing the browser window to {width}x{height}')
    # Splinter does not support window resize, so we must do it via driver instead
    # https://stackoverflow.com/a/21062539/148781
    context.page.browser.driver.set_window_size(width, height)
