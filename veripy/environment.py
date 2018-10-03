import logging

from behave import fixture, use_fixture
from behave.log_capture import capture
from behave.model_core import Status

import splinter

from . import settings
from .utils import mkdir

# bootstrap the custom types
from . import custom_types  # noqa


# Bootstrap the logger.
logging.basicConfig(**settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    """
    """
    if settings.BROWSER == 'remote':
        browser = splinter.Browser(
            driver_name='remote',
            browser='chrome',
            url=settings.SELENIUM_URL,
        )
    else:
        browser = splinter.Browser(
            driver_name=settings.BROWSER,
            headless=settings.RUN_HEADLESS,
        )
    context.browser = browser
    context.add_cleanup(browser.quit)
    return browser


@capture
def before_all(context):
    """ Before the suite runs, we set up a location to write temp files to and
    a directory for the report to be written to.
    """
    logger.debug('Setting up tmp directory and reports output directory.')
    context.tmp_directory = settings.TMP_DIR
    mkdir(settings.REPORTS_DIR)


@capture
def before_feature(context, feature):
    use_fixture(browser_chrome, context, timeout=10)


@capture
def before_scenario(context, scenario):
    """ Before each scenario, we need to restart the browser session so that
    there's no bleed-over from previous tests.
    """
    pass


@capture
def after_scenario(context, scenario):
    """ After each scenario, quit the browser session. """
    pass


@capture
def before_step(context, step):
    """ Here we inject the current step into the context so that the steps can
    add dynamic properties to it.
    """
    # TODO: Remove this line. This should be done in a proper step subclass or
    # something so that we can eventually add all kinds of things to the step.
    step.screenshots = []
    context.step = step


@capture
def after_step(context, step):
    """ Here we capture the screen if the step is a failure.
    """
    if step.status == Status.failed:
        from veripy.utils.browsers import screenshot_bytes
        step.screenshots.append(screenshot_bytes(context))
