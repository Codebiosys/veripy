import logging
import os.path
from behave import when
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('forms')


@when('the content from "{filename:file_input_type}" is entered into the "{element_name}"')
def when_file_content_entered(context, element_name, filename):
    """ Copies the text from the given filename and enters it into the target element
    ::

        When the content from "My File.md" has been entered into the "Markdown Editor"

    """
    logger.info(f'Entering content from "{filename}" into "{element_name}".')
    assert filename is not None, 'No file specified.'
    assert os.path.isfile(filename), 'The specified file does not exist.'

    with open(filename) as fp:
        content = fp.read()
    try:
        field = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    field.fill(content)
