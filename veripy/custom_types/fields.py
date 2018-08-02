from behave import register_type
import parse


@parse.with_pattern(r'(enabled|disabled)')
def parse_word_enabled_disabled(text):
    """Type converter for "enabled" or "disabled" (followed by one/more spaces)."""
    return text.strip()


register_type(field_enabled_option=parse_word_enabled_disabled)


@parse.with_pattern(r'(required|optional)')
def parse_word_required_optional(text):
    """Type converter for "required" or "optional" """
    return text.strip()


register_type(field_required_option=parse_word_required_optional)


@parse.with_pattern(r'(email|file|number|password|tel|text|url)[s]?')
def parse_word_field_type(text):
    """Type converter for input value types """
    return text.strip()


register_type(field_input_type=parse_word_field_type)
