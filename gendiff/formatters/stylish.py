INDENTS = '  '
PLUS = '+ '
MINUS = '- '


# def stylish_formatter(source, depth=0):
#     result = ['{']
#     for item in source:
#         match item['status']:
#             case 'nested':
#                 result.append(f"{INDENTS}{item['key']}")
#                 result.append(stylish_formatter(item['value'], depth + 1))
#             case 'added':
#                 result.append(f"{PLUS}{item['key']}:{item['value']}")
#             case 'deleted':
#                 result.append(f"{MINUS}{item['key']}:{item['value']}")
#             case 'unchanged':
#                 result.append(f"{INDENTS}{item['key']}:{item['value']}")
#             case 'changed':
#                 result.append(f"{MINUS}{item['key']}:{item['old value']}")
#                 result.append(f"{PLUS}{item['key']}:{item['new value']}")
#     result.append('}')
#     return '\n'.join(result)


def stylish_formatter(source, depth=1):
    result = ['{']
    for item in source:
        match item['status']:
            case 'nested':
                result.append(f"{INDENTS*2*depth}{item['key']}: {stylish_formatter(item['value'], depth+1)}")
            case 'added':
                result.append(f"{INDENTS*(2*depth-1)}{PLUS}{item['key']}: {psevdo_json(item['value'], depth+1)}")
            case 'deleted':
                result.append(f"{INDENTS*(2*depth-1)}{MINUS}{item['key']}: {psevdo_json(item['value'], depth+1)}")
            case 'unchanged':
                result.append(f"{INDENTS*2*depth}{item['key']}: {psevdo_json(item['value'], depth+1)}")
            case 'changed':
                result.append(f"{INDENTS*(2*depth-1)}{MINUS}{item['key']}: {psevdo_json(item['old value'], depth+1)}")
                result.append(f"{INDENTS*(2*depth-1)}{PLUS}{item['key']}: {psevdo_json(item['new value'], depth+1)}")
    result.append(f'{INDENTS*2*(depth-1)}}}')
    return '\n'.join(result)


def psevdo_json(structure, depth):
    match structure:
        case bool():
            return str(structure).lower()
        case None:
            return 'null'

        case dict():
            result = ['{']
            for key, value in structure.items():
                result.append(f'{INDENTS*2*depth}{key}: {psevdo_json(value, depth+1)}')
            result.append(f'{INDENTS*2*(depth-1)}}}')
            return '\n'.join(result)
        case _:
            return structure


# def generate_stylish_format(data_tree):
#     result = {}
#     for item in data_tree:
#         if item['status'] == 'nested':
#             result[f"{item['key']}"] = generate_stylish_format(item['value'])
#
#         elif item['status'] == 'added':
#             result[f"{PLUS}{item['key']}"] = item['value']
#         elif item['status'] == 'deleted':
#             result[f"{MINUS}{item['key']}"] = item['value']
#         elif item['status'] == 'unchanged':
#             result[f"{item['key']}"] = item['value']
#         elif item['status'] == 'changed':
#             result[f"{MINUS}{item['key']}"] = item['old value']
#             result[f"{PLUS}{item['key']}"] = item['new value']
#
#     return result
#
#
# def stylish_formatter(diff):
#     result = []
#     new_dumps = (json.dumps(
#         generate_stylish_format(diff),
#         separators=("", ": "),
#         indent=4)
#         .replace('"', "")
#          )
#     for item in new_dumps.split('\n'):
#         if item.lstrip().startswith(('+', '-')):
#             result.append(item[2:])
#         else:
#             result.append(item)
#
#     return '\n'.join(result)
