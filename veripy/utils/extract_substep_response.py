
def extract_substep_response(error):
    """
    Behave hides the message we want in another message, so we need to extract it:
    https://github.com/behave/behave/blob/644038147a8fcb4cb9de860156d85483a77b8f72/behave/runner.py#L401
    """
    error_messages = error.args[0].split('\n')
    try:
        error_response = error_messages.pop(1)  # We want the 2nd sentence
    except IndexError:
        # The message was Missing
        return "No message specified"
    return error_response.replace("Substep info: Assertion Failed:", '').strip()
