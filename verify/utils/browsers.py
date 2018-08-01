import base64
import os.path
import uuid

from . import mkdir, open_and_purge


def screenshot_bytes(context):
    """ Capture a screenshot of the browser's current context and return the
    data as a byte-string.

    :returns (data, type) A tuple of the data and the mime type.
    """
    mkdir(context.tmp_directory)
    scenario_file_path = os.path.join(
        context.tmp_directory,
        f'{uuid.uuid4().hex}.png'
    )
    context.browser.driver.save_screenshot(scenario_file_path)

    with open_and_purge(scenario_file_path, 'rb') as f:
        return f.read(), 'image/png'
