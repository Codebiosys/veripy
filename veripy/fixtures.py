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
    setup_scenarios = context.context_setup.get(name, None)

    if not setup_scenarios:
        logger.error(f'Setup Teardown was requested, but no context feature named {name} was found')
        return

    logger.info(f'Setup running for {name}')
    for scenario in setup_scenarios['setup']:
        if scenario.should_run():

            scenario_steps = ''
            for step in scenario.all_steps:
                scenario_steps += f'{step.keyword} {step.name}\n'
            context.execute_steps(scenario_steps)
            scenario.skip()

    if set_teardown:
        def cleanup_steps():
            logger.info(f'Teardown running for {name}')
            for scenario in setup_scenarios['teardown']:
                scenario_steps = ''
                for step in scenario.all_steps:
                    scenario_steps += f'{step.keyword} {step.name}\n'
                context.execute_steps(scenario_steps)

            for scenario in setup_scenarios['setup']:
                scenario.reset()

        context.add_cleanup(cleanup_steps)
    return
