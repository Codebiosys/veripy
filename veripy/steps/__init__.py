from behave import given, when, then

from aggregates import * # noqa
from capture import * # noqa
from content import * # noqa
from forms import * # noqa
from navigation import * # noqa


@given('we have behave installed')
def given_test(context):
    pass


@when('we implement a test')
def when_test(context):
    context.hello = 'YES'
    assert True is not False


@then('behave will test it for us!')
def then_test(context):
    assert context.failed is False
