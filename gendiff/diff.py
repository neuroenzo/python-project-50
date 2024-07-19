from gendiff.formats import build_formatter
from gendiff.parse_files import define_file_type


def generate_diff(first_file, second_file, format_name='stylish'):
    first_source = define_file_type(first_file)
    second_source = define_file_type(second_file)

    return build_formatter(first_source, second_source, format_name)
