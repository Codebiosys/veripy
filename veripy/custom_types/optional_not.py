from behave import register_type
from parse_type import TypeBuilder
import parse


@parse.with_pattern(r'not\s+')
def parse_word_not(text):
    """Type converter for "not " (followed by one/more spaces)."""
    return text.strip() == 'not'


parse_optional_word_not = TypeBuilder.with_optional(parse_word_not)
register_type(optional_not=parse_optional_word_not)


@parse.with_pattern(r"(es|s)?")
def parse_plural_word(text):
    """Type converter for "not " (followed by one/more spaces)."""
    return text.strip()


parse_optional_plural_word = TypeBuilder.with_optional(parse_plural_word)
register_type(optional_plural=parse_optional_plural_word)
