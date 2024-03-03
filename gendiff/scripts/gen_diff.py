import argparse

from gendiff.formatters.stylish import stylish_formatter
from gendiff.parse_files import generate_diff


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file')
    diff.add_argument('second_file')
    diff.add_argument('-f', '--format', help='set format of output')

    args = diff.parse_args()

    diff = generate_diff(args.first_file, args.second_file)

    print(stylish_formatter(diff))


if __name__ == '__main__':
    main()
