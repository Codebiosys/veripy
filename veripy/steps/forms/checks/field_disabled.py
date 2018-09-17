import logging
from behave import then
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('forms')


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
    not_ = bool(not_)
    logger.info(f'Asserting that "{field}" is {"not " if not_ else ""}{state}.')
    require_enabled = (state == 'enabled') != not_
    try:
        field = context.page[field]
    except context.page.ElementNotFound:
        raise AssertionError(f'The {field} was not found on the page')
    if require_enabled:
        assert not field._element.get_attribute('disabled'), \
            f'"{field}" is supposed to be enabled and it was not.'
    else:
        assert field._element.get_attribute('disabled'), (
            f'"{field}" is supposed to be disabled and it was not.'
        )
