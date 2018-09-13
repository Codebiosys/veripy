import logging
from behave import then
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('fields')


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
    not_ = bool(not_)
    logger.info(f'Asserting that "{field}" does {"not " if not_ else ""}accept {input_type}.')
    try:
        element = context.page[field]
    except context.page.ElementNotFound:
        raise AssertionError(f'The {field} was not found on the page')

    type = element._element.get_attribute('type')
    assert (type == input_type) != not_, (
        f'"{field}" is {"not " if not_ else ""}supposed to accept '
        f'{input_type} but did{"" if not_ else " not"}.'
    )
