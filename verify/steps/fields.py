from behave import *

from pages import Page


@when('"{text}" is entered into the {input_name}')
def enter_text_into_input(context, text, input_name):
    """ Tells the browser to enter the given test into an element with
    the given identifier.
    """
    input = getattr(context.page, input_name)
    input.fill(text)


@when('the user clicks the {element_name}')
def check_element(context, element_name):
    """ Tells the browser to click on an element with the given identifier. """
    element = getattr(context.page, element_name)
    element.click()

