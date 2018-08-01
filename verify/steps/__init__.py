from behave import *

from pages import Page


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    context.hello = 'YES'
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


