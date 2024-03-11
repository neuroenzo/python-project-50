import json
import yaml

from pathlib import Path


def define_file_type(file_name):
    with open(file_name) as f:
        data = f.read()
    match Path(file_name).suffix:
        case '.json':
            return json.loads(data)
        case '.yml' | '.yaml':
            return yaml.safe_load(data)


def build_source_tree(first_source, second_source):
    tree = []
    keys = sorted(first_source.keys() | second_source.keys())

    for key in keys:
        if key not in first_source.keys():
            tree.append(
                {
                    'status': 'added',
                    'key': key,
                    'value': second_source.get(key),
                }
            )
        elif key not in second_source.keys():
            tree.append(
                {
                    'status': 'deleted',
                    'key': key,
                    'value': first_source.get(key)
                }
            )
        elif (isinstance(first_source.get(key), dict)
              and isinstance(second_source.get(key), dict)):
            tree.append(
                {
                    'status': 'nested',
                    'key': key,
                    'value': build_source_tree(
                        first_source.get(key),
                        second_source.get(key)
                    )
                }
            )
        elif first_source.get(key) == second_source.get(key):
            tree.append(
                {
                    'status': 'unchanged',
                    'key': key,
                    'value': first_source.get(key)
                }
            )
        else:
            tree.append(
                {
                    'status': 'changed',
                    'key': key,
                    'old value': first_source.get(key),
                    'new value': second_source.get(key)
                }
            )

    return tree


def generate_diff(first_file, second_file):
    first_source = define_file_type(first_file)
    second_source = define_file_type(second_file)

    return build_source_tree(first_source, second_source)
