from behave import when, then


# When


@when('"{text}" is entered into the {input_name}')
def enter_text_into_input(context, text, input_name):
    """ Tells the browser to enter the given test into an element with
    the given identifier.
    """
    input = context.page[input_name]
    input.fill(text)


@when('the user clicks the {element_name}')
def click_element(context, element_name):
    """ Tells the browser to click on an element with the given identifier. """
    element = context.page[element_name]
    element.click()


# Then


@then('the {field} field is {not_:optional_not}{state:field_required_option}')
def field_is_required(context, field, not_, state):
    """ Require that if a field is required or optional in a form. """
    required = (state == 'required') != not_
    field = context.page[field]
    if required:
        assert field._element.get_attribute('required')
    else:
        assert not field._element.get_attribute('required')


@then('the {field} field is {not_:optional_not}{state:field_enabled_option}')
def field_is_enabled(context, field, not_, state):
    require_enabled = (state == 'enabled') != not_
    field = context.page[field]
    if require_enabled:
        assert not field._element.get_attribute('disabled')
    else:
        assert field._element.get_attribute('disabled')


@then('the {field} field does {not_:optional_not}accept {input_type:field_input_type}')
def field_accepts_type(context, field, not_, input_type):
    field = context.page[field]
    type = field._element.get_attribute('type')
    # Assert that the input-type equals the type or that they don't match.
    assert (type == input_type) != not_
