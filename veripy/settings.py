# Settings.py
# A global list of settings from the environment or hard coded that are useful
# throughout the application environment.


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Environment Definitions


class ENVIRONMENTS(object):
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'
    CI = 'ci'


ENVIRONMENT = os.environ['ENVIRONMENT']


# Browser Configuration


BROWSER = os.environ.get('BROWSER', 'chrome')
if BROWSER == 'remote':
    SELENIUM_URL = os.environ['SELENIUM_URL']

# We always run headless in CI mode. Otherwise we defer to the environment.
RUN_HEADLESS = (
    True if ENVIRONMENT == ENVIRONMENTS.CI else
    bool(os.environ.get('RUN_HEADLESS', False))
)


# File Storage Configuration


# A place for the test runner to store temporary files (like screenshots)
# during test runs.
TMP_DIRECTORY = os.environ.get('TMP_DIRECTORY', '/tmp/behave')

# Where to put the output reports.
REPORTS_DIRECTORY = os.environ.get('REPORTS_DIRECTORY', '../reports')

FIXTURES_DIR = os.environ.get('FIXTURES_DIR', os.path.join(BASE_DIR, 'pages', 'fixtures'))
RESOURCES_DIR = os.environ.get('RESOURCES_DIR', os.path.join(BASE_DIR, 'resources'))


# Logging

LOGGING_CONFIG = {
    'filename': 'veripy.log',
    'level': 'DEBUG',
}
