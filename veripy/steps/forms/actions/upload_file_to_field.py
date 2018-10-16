import logging
import os.path

from behave import when
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('forms')


@when('the file "{filename:file_input_type}" has been added to the "{element_name}"')
def when_upload_file_to_field(context, element_name, filename):
    """ Given that the desired file is located in the ``RESOURCES_DIR`` this
    statement allows the user to add a file to a file input in a form.

    ::

        When the "My File.txt" has been added to the "File Upload Field"

    """
    logger.info(f'Uploading "{filename}" to "{element_name}".')
    assert filename is not None, 'The filename given was not found.'
    assert os.path.isfile(filename), 'The specified file does not exist.'

    try:
        field = context.page[element_name]
    except context.page.ElementNotFound:
        raise AssertionError(f'The "{element_name}" was not found on the page.')

    field._element.send_keys(filename)
    context.step.stored_value = filename
