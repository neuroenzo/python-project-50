import json
import os
import yaml

from pathlib import Path


def define_file_type(file_name):
    file_path = (os.path.
                 join(Path(__file__)
                      .resolve()
                      .parent
                      .parent,
                      f'tests/fixtures/{file_name}'))
    with open(file_path) as f:
        data = f.read()
    match Path(file_path).suffix:
        case '.json':
            return json.loads(data)
        case '.yml':
            return yaml.safe_load(data)


def generate_diff(file1, file2):
    first_source = define_file_type(file1)
    second_source = define_file_type(file2)

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
