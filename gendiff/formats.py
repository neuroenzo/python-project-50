from .formatters.stylish import make_stylish_formatter
from .formatters.plain import make_plain_formatter
from .formatters.json import make_raw_json
from .ast import build_source_tree


def build_formatter(first_source, second_source, format_name):
    if format_name == 'stylish':
        return make_stylish_formatter(
            build_source_tree(first_source, second_source)
        )
    elif format_name == 'plain':
        return make_plain_formatter(
            build_source_tree(first_source, second_source)
        )
    elif format_name == 'json':
        return make_raw_json(
            build_source_tree(first_source, second_source)
        )
    else:
        raise TypeError(f'{format_name} is not available format')
