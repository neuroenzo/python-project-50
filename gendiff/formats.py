from utils.custom_exceptions import FileFormatError
from .formatters.stylish import build_stylish
from .formatters.plain import build_plain
from .formatters.json import build_raw_json
from .ast import build_source_tree


def build_formatter(first_source, second_source, format_name):
    if format_name == 'stylish':
        return build_stylish(
            build_source_tree(first_source, second_source)
        )
    elif format_name == 'plain':
        return build_plain(
            build_source_tree(first_source, second_source)
        )
    elif format_name == 'json':
        return build_raw_json(
            build_source_tree(first_source, second_source)
        )
    else:
        raise TypeError(f'{format_name} is not available format')
