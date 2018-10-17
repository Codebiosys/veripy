import os
import logging

from behave import fixture
from behave.runner_util import parse_features, collect_feature_locations

import splinter

from . import settings

# bootstrap the custom types
from . import custom_types  # noqa

# Bootstrap the logger.
logging.basicConfig(**settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


@fixture
def collect_setup_files(context):
    """
    Searches feature files in 'setup' directory for any configured setup features
    and adds them to the context of the current run. This is done before_all so
    that the setup features are available during the run.
    """
    setup_files = os.path.join(context.config.base_dir, settings.SETUP_DIR)
    logger.info(f'Parsing setup files from the {setup_files} directory.')

    setup_locations = collect_feature_locations([setup_files])
    setup_features = parse_features(setup_locations)
    context_setup = {}
    for feature in setup_features:
        tag_name = None
        for tag in feature.tags:
            if 'configure' in tag:
                tag_name = tag.replace('configure.', '')
                break
        logger.info(f'Setting Context Setup {tag_name} from {feature.location}.')

        setup = {
            'setup': [],
            'teardown': []}
        for scenario in feature.scenarios:
            if any(tag == 'teardown' for tag in scenario.tags):
                logger.info(f'Setting teardown from {scenario.location}.')
                setup['teardown'].append(scenario)
            else:
                logger.info(f'Setting setup from {scenario.location}.')
                setup['setup'].append(scenario)
        context_setup[tag_name] = setup
    context.context_setup = context_setup


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    """
    Adds a browser to the current context. Adds a cleanup step to quit the browser
    on end/fail
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
    """
    Based on a tag request (e.g. - @fixture.setup.{name}), run the steps of the
    @configure.{name} setup feature if the setup feature has not been previously
    run. Adds a cleanup step after the feature/scenario if set_teardown is True
    """
    setup_scenarios = context.context_setup.get(name, None)

    if not setup_scenarios:
        logger.error(f'Setup Teardown was requested, but no context feature named {name} was found')
        return

    logger.info(f'Setup running for {name}')

    def execute_scenario_steps(scenario):
        scenario_steps = ''
        for step in scenario.all_steps:
            scenario_steps += f'{step.keyword} {step.name}\n'
        context.execute_steps(scenario_steps)

    for scenario in setup_scenarios['setup']:
        if scenario.should_run():
            if scenario.type == 'scenario_outline':
                for sub_scenario in scenario.scenarios:
                    execute_scenario_steps(sub_scenario)
            else:
                execute_scenario_steps(scenario)
            scenario.skip()

    if set_teardown:
        def cleanup_steps():
            logger.info(f'Teardown running for {name}')
            for scenario in setup_scenarios['teardown']:
                if scenario.type == 'scenario_outline':
                    for sub_scenario in scenario.scenarios:
                        execute_scenario_steps(sub_scenario)
                else:
                    execute_scenario_steps(scenario)

            for scenario in setup_scenarios['setup']:
                scenario.reset()

        context.add_cleanup(cleanup_steps)
    return
