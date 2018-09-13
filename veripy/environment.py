import logging

from behave.log_capture import capture
from behave.model_core import Status

import splinter

from veripy.utils import mkdir
from veripy import settings

# bootstrap the custom types
from veripy import custom_types  # noqa


# Bootstrap the logger.
logging.basicConfig(**settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@capture
def before_all(context):
    """ Before the suite runs, we set up a location to write temp files to and
    a directory for the report to be written to.
    """
    logger.debug('Setting up tmp directory and reports output directory.')
    context.tmp_directory = settings.TMP_DIRECTORY
    mkdir(settings.REPORTS_DIRECTORY)


@capture
def before_scenario(context, scenario):
    """ Before each scenario, we need to restart the browser session so that
    there's no bleed-over from previous tests.
    """
    if settings.BROWSER == 'remote':
        context.browser = splinter.Browser(
            driver_name='remote',
            browser='chrome',
            url=settings.SELENIUM_URL,
        )
    else:
        context.browser = splinter.Browser(
            driver_name=settings.BROWSER,
            headless=settings.RUN_HEADLESS,
        )


@capture
def after_scenario(context, scenario):
    """ After each scenario, quit the browser session. """
    context.browser.quit()


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
