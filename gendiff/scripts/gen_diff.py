from gendiff.diff import generate_diff
from gendiff.cli import parse_arguments


def main():
    arguments = parse_arguments()
    first_file = arguments.first_file
    second_file = arguments.second_file
    format_name = arguments.format_name

    print(generate_diff(first_file, second_file, format_name))


if __name__ == '__main__':
    main()
