import logging
from behave import then

from veripy import custom_types  # noqa
from veripy.utils.extract_substep_response import extract_substep_response

logger = logging.getLogger('aggregates')


@then('the statement that \'{sentence}\' responds with')
def check_assertion(context, sentence):
    ''' Asserts that the given sentence raises an exception with the given message
    ::

        the statement that 'the "Home Link" is visible' responds with
        """The element "Home Link" was supposed to be visible and was not."""
    '''
    message = context.text
    logger.info(f'Asserting that the sentence \'{sentence}\' raises the message \'{message}\'')
    try:
        context.execute_steps(f"""
        Then {sentence}
        """)
    except AssertionError as error:
        newMessage = extract_substep_response(error)

        assert newMessage.strip() == message.strip(), f"""
            The statement \'{sentence}\' should have responded with {message},
            but responded with {newMessage}"""
    else:
        raise AssertionError(f'The statement \'{sentence}\' should have responded with '
                             '\'{message\', but it did not')
