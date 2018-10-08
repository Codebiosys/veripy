import os
import logging

from behave import fixture, use_fixture
from behave.log_capture import capture
from behave.model_core import Status
from behave.runner_util import parse_features, collect_feature_locations

import splinter

from . import settings
from .utils import mkdir

# bootstrap the custom types
from . import custom_types  # noqa

# Bootstrap the logger.
logging.basicConfig(**settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@fixture
def collect_setup_files(context):
    setup_files = os.path.join(context.config.base_dir, settings.SETUP_DIR)
    setup_locations = collect_feature_locations([setup_files])
    setup_features = parse_features(setup_locations)
    context_setup = {}
    for feature in setup_features:
        tag_name = None
        for tag in feature.tags:
            if 'configure' in tag:
                tag_name = tag.replace('configure.', '')
                break
        setup = {
            'setup': [],
            'teardown': []}
        for scenario in feature.scenarios:
            if any(tag == 'teardown' for tag in scenario.tags):
                setup['teardown'].append(scenario)
            else:
                setup['setup'].append(scenario)
        context_setup[tag_name] = setup
    context.context_setup = context_setup


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


@fixture
def setup_teardown(context, name, set_teardown=False):
    setup_scenarios = context.context_setup.get(name)

    for scenario in setup_scenarios['setup']:
        if scenario.should_run():
            scenario_steps = ''
            for step in scenario.all_steps:
                scenario_steps += f'{step.keyword} {step.name}\n'
            context.execute_steps(scenario_steps)
            scenario.skip()

    if set_teardown:
        def cleanup_steps():
            for scenario in setup_scenarios['teardown']:
                scenario_steps = ''
                for step in scenario.all_steps:
                    scenario_steps += f'{step.keyword} {step.name}\n'
                context.execute_steps(scenario_steps)

            for scenario in setup_scenarios['setup']:
                scenario.reset()

        context.add_cleanup(cleanup_steps)


@capture
def before_all(context):
    """ Before the suite runs, we set up a location to write temp files to and
    a directory for the report to be written to.
    """
    logger.debug('Setting up tmp directory and reports output directory.')
    context.tmp_directory = settings.TMP_DIR
    mkdir(settings.REPORTS_DIR)

    if settings.SETUP_DIR:
        use_fixture(collect_setup_files, context)


@capture
def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context, timeout=10)
    if tag.startswith("fixture.setup.teardown"):
        name = tag.replace("fixture.setup.teardown.", "")
        use_fixture(setup_teardown, context, name, set_teardown=True)
    elif tag.startswith("fixture.setup"):
        name = tag.replace("fixture.setup.", "")
        use_fixture(setup_teardown, context, name, set_teardown=False)


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
    # from pprint import pprint as pp
    # import pdb; pdb.set_trace()
    step.screenshots = []
    context.step = step


@capture
def after_step(context, step):
    """ Here we capture the screen if the step is a failure.
    """
    if step.status == Status.failed:
        from veripy.utils.browsers import screenshot_bytes
        step.screenshots.append(screenshot_bytes(context))
