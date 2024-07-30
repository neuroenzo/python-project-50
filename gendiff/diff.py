from gendiff.formats import build_formatter
from gendiff.parse_files import get_data


def generate_diff(first_file, second_file, format_name='stylish'):
    first_source = get_data(first_file)
    second_source = get_data(second_file)

    return build_formatter(first_source, second_source, format_name)
