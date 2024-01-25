import argparse
import json
import os

from pathlib import Path


first_file = os.path.join(Path(__file__)
                          .resolve().parent.parent.parent,
                          'tests/fixtures/flat1.json')
second_file = os.path.join(Path(__file__)
                           .resolve().parent.parent.parent,
                           'tests/fixtures/flat2.json')


def generate_diff(file1, file2):
    with (
        open(file1, "r", encoding="utf-8") as f1,
        open(file2, "r", encoding="utf-8") as f2,
    ):
        first_source = json.load(f1)
        second_source = json.load(f2)

        keys = sorted(set(first_source.keys()) | set(second_source.keys()))
        result = "{\n"
        for key in keys:
            if key in first_source and key not in second_source:
                result += f'- {key}: {str(first_source[key]).lower()}\n'
            elif key in second_source and key not in first_source:
                result += f'+ {key}: {str(second_source[key]).lower()}\n'
            elif key in first_source and key in second_source\
                    and first_source[key] != second_source[key]:
                result += f'- {key}: {first_source[key]}\n+' \
                          f' {key}: {second_source[key]}\n'
            elif key in first_source and key in second_source:
                result += f'  {key}: {first_source[key]}\n'
        result += "}"

        print(result)

        return result


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file')
    diff.add_argument('second_file')
    diff.add_argument('-f', '--format', help='set format of output')

    diff.parse_args()

    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
