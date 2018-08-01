import os

from behave.log_capture import capture
import splinter

from utils import mkdir


@capture
def before_all(context):
    context.tmp_directory = '/tmp/behave'
    mkdir('../report')


@capture
def before_scenario(context, scenario):
    context.browser = splinter.Browser(driver_name=os.getenv('BROWSER', 'chrome'))


@capture
def after_scenario(context, scenario):
    context.browser.quit()


@capture
def before_step(context, step):
    step.screenshots = []
    context.step = step
