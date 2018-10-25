import logging
from behave import then

from veripy import custom_types  # noqa


logger = logging.getLogger('aggregates')


@then('it is not the case that {sentence}')
def invert_sentence(context, sentence):
    """ Asserts that the given sentence is not true
    ::

        it is not the case that the "Home Link" is visible
    """
    logger.info(f'Asserting that the following is not true: {sentence}')
    if getattr(context, 'table', None) is not None:
        raise AssertionError(f'Tabular instructions are not supported by compound sentences.')

    try:
        context.execute_steps(f"""
        Then {sentence}
        """)
    except AssertionError:
        pass
    else:
        raise AssertionError(f'it should not be the case that {sentence}, but it was so')
