import json

INDENTS = '  '
PLUS = '+ '
MINUS = '- '


def generate_stylish_format(data_tree):
    result = {}
    for item in data_tree:
        if item['status'] == 'nested':
            result[f"{item['key']}"] = generate_stylish_format(item['value'])

        elif item['status'] == 'added':
            result[f"{PLUS}{item['key']}"] = item['value']
        elif item['status'] == 'deleted':
            result[f"{MINUS}{item['key']}"] = item['value']
        elif item['status'] == 'unchanged':
            result[f"{item['key']}"] = item['value']
        elif item['status'] == 'changed':
            result[f"{MINUS}{item['key']}"] = item['old value']
            result[f"{PLUS}{item['key']}"] = item['new value']

    return result


def stylish_formatter(diff):
    result = []
    new_dumps = (json.dumps(
        generate_stylish_format(diff),
        separators=("", ": "),
        indent=4)
        .replace('"', "")
         )
    for item in new_dumps.split('\n'):
        if item.lstrip().startswith(('+', '-')):
            result.append(item[2:])
        else:
            result.append(item)

    return '\n'.join(result)
