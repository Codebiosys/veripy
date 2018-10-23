import os
import logging

from behave import fixture
from behave.runner import scoped_context_layer
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

    feature_locations = collect_feature_locations([setup_files])
    all_features = parse_features(feature_locations)
    context_setup = {}
    for feature in all_features:
        tag_name = None
        for tag in feature.tags:
            if tag.startswith('configure.'):
                tag_name = tag.replace('configure.', '')
                break
        if not tag_name:
            # This was not a configuration, so skip the feature
            continue
        logger.info(f'Setting Context Setup {tag_name} from {feature.location}.')
        setup = {
            'setup': [],
            'teardown': []}
        for scenario in feature.scenarios:
            if any(tag == 'teardown' for tag in scenario.tags):
                logger.info(f'Setting teardown from {scenario.location}.')
                setup['teardown'].append(scenario)
            elif any(tag == 'setup' for tag in scenario.tags):
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


def execute_scenario_steps(local_scenario, scenario):
    scenario_steps = ''
    for step in scenario.steps:
        scenario_steps += f'{step.keyword} {step.name}\n'
    local_scenario.execute_steps(scenario_steps)


def run_scenario(local_context, scenario):
    for tag in scenario.tags:
        local_context._runner.hooks['before_tag'](local_context, tag)
    local_context._runner.hooks['before_scenario'](local_context, scenario)
    if scenario.background:
        execute_scenario_steps(local_context, scenario.background)
    if scenario.type == 'scenario_outline':
        for sub_scenario in scenario.scenarios:
            execute_scenario_steps(local_context, sub_scenario)
    else:
        execute_scenario_steps(local_context, scenario)
    local_context._runner.hooks['after_scenario'](local_context, scenario)
    for tag in scenario.tags:
        local_context._runner.hooks['after_tag'](local_context, tag)


@fixture
def setup_teardown(context, name, set_teardown=False, teardown_only=False):
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

    if not teardown_only:
        for scenario in setup_scenarios['setup']:
            if scenario.should_run():
                if any(tag.startswith('fixture.browser') for tag in scenario.tags):
                    with scoped_context_layer(context, layer_name='setup_teardown'):
                        run_scenario(context, scenario)
                else:
                    run_scenario(context, scenario)
                scenario.skip()

    if set_teardown:
        def cleanup_steps():
            logger.info(f'Teardown running for {name}')
            for scenario in setup_scenarios['teardown']:
                if any(tag.startswith('fixture.browser') for tag in scenario.tags):
                    with scoped_context_layer(context, layer_name='setup_teardown'):
                        run_scenario(context, scenario)
                else:
                    run_scenario(context, scenario)
            for scenario in setup_scenarios['setup']:
                scenario.reset()

        context.add_cleanup(cleanup_steps)
    return
