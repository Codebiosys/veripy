import logging

from behave import use_fixture
from behave.log_capture import capture
from behave.model_core import Status
from selenium.common.exceptions import UnexpectedAlertPresentException

from . import settings, fixtures
from .utils import mkdir

# bootstrap the custom types
from . import custom_types  # noqa

# Bootstrap the logger.
logging.basicConfig(**settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@capture
def before_all(context):
    """ Before the suite runs, we set up a location to write temp files to and
    a directory for the report to be written to.
    """
    logger.debug('Setting up tmp directory and reports output directory.')
    context.tmp_directory = settings.TMP_DIR
    mkdir(settings.REPORTS_DIR)

    if settings.SETUP_DIR:
        use_fixture(fixtures.collect_setup_files, context)


@capture
def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(fixtures.browser_chrome, context, timeout=10)
    if tag.startswith("fixture.setup.teardown"):
        name = tag.replace("fixture.setup.teardown.", "")
        use_fixture(fixtures.setup_teardown, context, name, set_teardown=True)
    elif tag.startswith("fixture.setup"):
        name = tag.replace("fixture.setup.", "")
        use_fixture(fixtures.setup_teardown, context, name, set_teardown=False)
    elif tag.startswith("fixture.teardown"):
        name = tag.replace("fixture.teardown.", "")
        use_fixture(fixtures.setup_teardown, context, name, set_teardown=True, teardown_only=True)


@capture
def after_tag(context, tag):
    """
    """
    pass


@capture
def before_feature(context, feature):
    """ Before each feature.
    """
    pass


@capture
def after_feature(context, feature):
    """ After each feature.
    """
    pass


@capture
def before_scenario(context, scenario):
    """ Before each scenario.
    """
    if hasattr(context, 'active_outline') and context.active_outline:
        scenario.row = context.active_outline
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
    if step.status == Status.failed and hasattr(context, 'browser'):
        try:
            from veripy.utils.browsers import screenshot_bytes
            step.screenshots.append(screenshot_bytes(context))
        except UnexpectedAlertPresentException:
            step.stored_value = "Capturing a screenshot of a browser alert is not supported."
