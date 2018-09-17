import logging
from behave import when
# Bootstrap the custom types for Sphinx
from veripy import custom_types  # noqa

logger = logging.getLogger('forms')


@when('the file "{filename:file_input_type}" has been added to the "{field}" field')
def when_upload_file_to_field(context, field, filename):
    """ Given that the desired file is located in the ``RESOURCES_DIR`` this
    statement allows the user to add a file to a file input in a form.
    ::

        When the "My File.txt" has been added to the "File Upload" field

    """
    logger.info(f'Uploading "{filename}" to "{field}".')
    assert filename is not None, 'The filename given was not found.'

    try:
        field = context.page[field]
    except context.page.ElementNotFound:
        raise AssertionError(f'The {field} was not found on the page')

    field._element.send_keys(filename)
    context.step.stored_value = filename
