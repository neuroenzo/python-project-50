import argparse

from gendiff.parse_files import generate_diff


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file')
    diff.add_argument('second_file')
    diff.add_argument('-f',
                      '--format_name',
                      help='set format of output',
                      default='stylish')

    args = diff.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format_name))


if __name__ == '__main__':
    main()
