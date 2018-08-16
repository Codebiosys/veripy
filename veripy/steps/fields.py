from behave import given, when, then

# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa


# When


@given('"{text}" is entered into the "{input_name}"')
@when('"{text}" is entered into the "{input_name}"')
def when_enter_text_into_input(context, text, input_name):
    """ Tells the browser to enter the given test into an element with
    the given identifier.
    ::

        When "query text" is entered into the "Search Box"

    """
    input = context.page[input_name]
    input.fill(text)


@given('the user clicks the "{element_name}"')
@when('the user clicks the "{element_name}"')
def when_click_element(context, element_name):
    """ Tells the browser to click on an element with the given identifier.
    ::

        When the user clicks the "Search Button"
    """
    element = context.page[element_name]
    element.click()


@when('the file "{filename:file_input_type}" has been added to the "{field}" field')
def when_upload_file_to_field(context, field, filename):
    """ Given that the desired file is located in the ``RESOURCES_DIR`` this
    statement allows the user to add a file to a file input in a form.
    ::

        When the "My File.txt" has been added to the "File Upload" field

    """
    assert filename is not None

    field = context.page[field]
    field._element.send_keys(filename)


# Then


@then('the "{field}" field is {not_:optional_not}{state:field_required_option}')
def then_field_is_required(context, field, not_, state):
    """ Require that a field is required or optional in a form.
    This sentence allows the user to specify their requirements in natural
    language.

    - Users can specify that a field is either "required" or "optional"
    - Users can use the word "not".

    ::

        # These have the same effect.
        The "Phone Number" field is not required
        The "Phone Number" field is optional

    """
    required = (state == 'required') != not_
    field = context.page[field]
    if required:
        assert field._element.get_attribute('required')
    else:
        assert not field._element.get_attribute('required')


@then('the "{field}" field is {not_:optional_not}{state:field_enabled_option}')
def then_field_is_enabled(context, field, not_, state):
    """ Require that a field is enabled or disabled in a form.
    This sentence allows the user to specify their requirements in natural
    language.

    - Users can specify that a field is either "enabled" or "disabled"
    - Users can use the word "not".

    ::

        # These have the same effect.
        The "Phone Number" field is not enabled
        The "Phone Number" field is disabled

    """
    require_enabled = (state == 'enabled') != not_
    field = context.page[field]
    if require_enabled:
        assert not field._element.get_attribute('disabled')
    else:
        assert field._element.get_attribute('disabled')


@then('the "{field}" field does {not_:optional_not}accept {input_type:field_input_type}')
def then_field_accepts_type(context, field, not_, input_type):
    """ Require that a field be configured to accept or not accept certain input types.
    This sentence allows the user to specify their requirements in natural
    language.

    - Users can specify that a field accepts any typical HTML input type.
    - Users can use the word "not".
    - Input types can be plural. (``number`` & ``numbers`` have the same effect)

    ::

        # These have the same effect.
        The "Phone Number" field does accept text
        The "Phone Number" field does not accept numbers

    """
    field = context.page[field]
    type = field._element.get_attribute('type')
    # Assert that the input-type equals the type or that they don't match.
    assert (type == input_type) != not_
