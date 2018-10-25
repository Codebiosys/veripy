import logging
from behave import then

from veripy import custom_types  # noqa
from veripy.utils.extract_substep_response import extract_substep_response

logger = logging.getLogger('aggregates')


@then('if \'{sentence}\', the system responds with')
def check_action(context, sentence):
    ''' Asserts that the given sentence raises an exception with the given message
    ::

        if 'the user clears the "Missing Field"', the system responds with
        """The element "Home Link" was supposed to be visible and was not."""
    '''
    if getattr(context, 'table', None) is not None:
        raise AssertionError(f'Tabular instructions are not supported by compound sentences.')

    message = context.text
    logger.info(f'Asserting that the sentence \'{sentence}\' raises the message \'{message}\'')
    try:
        context.execute_steps(f"""
        When {sentence}
        """)
    except AssertionError as error:
        newMessage = extract_substep_response(error)

        assert newMessage.strip() == message.strip(), f"""
            The statement \'{sentence}\' should have responded with {message},
            but responded with {newMessage}"""
    else:
        raise AssertionError(f'The statement \'{sentence}\' should have responded with '
                             '\'{message\', but it did not')
