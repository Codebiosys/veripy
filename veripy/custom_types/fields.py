import os.path

from behave import register_type
import parse

from veripy import settings


@parse.with_pattern(r'(enabled|disabled)')
def parse_word_enabled_disabled(text):
    """ Enables the use of ``enabled`` and ``disabled`` in sentences.
    The value of the property given to the step function is the text ``enabled``
    or ``disabled``.

    Use this type by annotating your variable with the ``field_enabled_option``.

    **Usage**
    ::

        @then('the search_button is {state:field_enabled_option}')
        def test_method(context, state):
            pass

    """
    return text.strip()


register_type(field_enabled_option=parse_word_enabled_disabled)


@parse.with_pattern(r'(required|optional)')
def parse_word_required_optional(text):
    """ Enables the use of ``required`` and ``optional`` in sentences.
    The value of the property given to the step function is the text ``required``
    or ``optional``.

    Use this type by annotating your variable with the ``field_required_option``.

    **Usage**
    ::

        @then('the phone_number is {state:field_required_option}')
        def test_method(context, state):
            pass

    """
    return text.strip()


register_type(field_required_option=parse_word_required_optional)


@parse.with_pattern(r'(email|file|number|password|tel|text|url|file)[s]?')
def parse_word_field_type(text):
    """ Use this type to match common HTML input field types. This type allows
    for an optional ``s`` to be added by the user to the name of the HTML input
    types. This value is not passed to the handler function.

    Use this type by annotating your variable with the ``field_input_type``.

    **Usage**
    ::

        @then('the field accepts {type_:field_input_type}')
        def test_method(context, type_):
            pass

    **Valid Types**

    Any of the following types are available: ``email``, ``file``, ``number``,
    ``password``, ``tel``, ``text``, ``url``, ``file`` as well as their plural
    counterparts (i.e. ``passwords``).
    """
    return text.strip()


register_type(field_input_type=parse_word_field_type)


@parse.with_pattern(r'([a-zA-Z\-]+\.[a-zA-Z0-9]+)')
def parse_word_file_name(filename):
    """ This type matches filenames.

    Use this type by annotating your variable with the ``file_input_type``.

    **Usage**
    ::

        @then('the file is called {filename:file_input_type}')
        def test_method(context, filename):
            pass

    **Important:** Filenames must contain an extension and at least 1 character
    before the ``.``.

    **Valid Filenames**

    - ``MyFile.txt``
    - ``my_file.md``

    **Invalid Filenames**

    - ``.bashrc``
    - ``python3``

    """
    return os.path.join(settings.RESOURCES_DIR, filename)


register_type(file_input_type=parse_word_file_name)
