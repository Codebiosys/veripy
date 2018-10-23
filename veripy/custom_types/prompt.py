from behave import register_type
import parse


@parse.with_pattern(r"(accepted|confirmed|cancelled|dismissed)")
def prompt_action_type(text):
    """ Captures the alert type.

    Use this type by annotating your variable with the ``prompt_action``.

    **Usage**
    ::

        @then('the prompt is {action:prompt_action}')
        def test_method(context, action):
            pass

    """
    return text.strip()


register_type(prompt_action=prompt_action_type)
