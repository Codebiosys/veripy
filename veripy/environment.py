from behave.log_capture import capture
import splinter

from utils import mkdir
import settings


@capture
def before_all(context):
    """ Before the suite runs, we set up a location to write temp files to and
    a directory for the report to be written to.
    """
    context.tmp_directory = settings.TMP_DIRECTORY
    mkdir(settings.REPORTS_DIRECTORY)


@capture
def before_scenario(context, scenario):
    """ Before each scenario, we need to restart the browser session so that
    there's no bleed-over from previous tests.
    """
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
