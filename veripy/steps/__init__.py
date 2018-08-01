from behave import given, when, then


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
