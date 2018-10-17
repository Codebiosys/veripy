import logging
from behave import then
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('forms')


@then('the "{element_name}" field is {not_:optional_not}{state:field_required_option}')
def then_field_is_required(context, element_name, not_, state):
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
    not_ = bool(not_)
    logger.info(f'Asserting that "{element_name}" is {"not " if not_ else ""}{state}.')
    required = (state == 'required') != not_
    try:
        element = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    if required:
        assert element._element.get_attribute('required'), (
            f'"{element_name}" is supposed to be required and it was not.'
        )
    else:
        assert not element._element.get_attribute('required'), (
            f'"{element_name}" is supposed to be optional and it was not.'
        )
