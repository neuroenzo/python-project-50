SPACES = '....'
PLUS = '+ '
MINUS = '- '


def s_formatter(data_tree, depth=0, result=None):
    if result is None:
        result = []

    result.append('{}{{'.format(SPACES*depth))

    for item in data_tree:
        if item['status'] == 'nested':
            step_inside = depth + 1
            result.append('{}{}: {{'.format(SPACES*step_inside, item['key']))
            if isinstance(item['value'], list):
                s_formatter(item['value'], step_inside, result)

        if item['status'] == 'added':
            result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['value']}')
        elif item['status'] == 'deleted':
            result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['value']}')
        elif item['status'] == 'unchanged':
            result.append(f'{SPACES*depth}  {item['key']}: {item['value']}')
        elif item['status'] == 'changed':
            result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['old value']}')
            result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['new value']}')

    result.append('}')

    return result

# import json


# def s_formatter(data_tree, depth=0, result=None):
#     if result is None:
#         result = ['{']
#         #result.append('{}{{'.format(SPACES*depth))
#
#     for item in data_tree:
#         if item['status'] == 'nested':
#             step_inside = depth + 1
#             result.append('{}{}: {{'.format(SPACES*step_inside, item['key']))
#             if isinstance(item['value'], list):
#                 s_formatter(item['value'], step_inside, result)
#
#         if item['status'] == 'added':
#             if isinstance(item['value'], dict):
#                 #result.append('{}{}{}: {{\n {}'.format(SPACES * depth, PLUS, item['key'], item['value']))
#
#                 result.append(f'{SPACES * depth}{PLUS}{item['key']}: {item['value']}')
#                 json.dumps(result, indent=4)
#             else:
#                 result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['value']}')
#         elif item['status'] == 'deleted':
#             result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['value']}')
#         elif item['status'] == 'unchanged':
#             result.append(f'{SPACES*depth}  {item['key']}: {item['value']}')
#         elif item['status'] == 'changed':
#             result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['old value']}')
#             result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['new value']}')
#
#     result.append('{}}}'.format(SPACES * depth))
#     json_data = json.dumps(result, indent=4)
#     print(json_data)
#     return json_data


# def s_formatter(data_tree, depth=0, result=None):
#     if result is None:
#         result = []
#
#     for item in data_tree:
#         if item['status'] == 'nested':
#             step_inside = depth + 1
#             result.append('{}{}: {{'.format(SPACES*step_inside, item['key']))
#             if isinstance(item['value'], list):
#                 s_formatter(item['value'], step_inside, result)
#
#         if item['status'] == 'added':
#             if isinstance(item['value'], dict):
#                 result.append('{}{}{}: {{\n {}'.format(SPACES * depth, PLUS, item['key'], item['value']))
#
#                 result.append(f'{item['key']}: {item['value']}')
#             else:
#                 result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['value']}')
#         elif item['status'] == 'deleted':
#             result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['value']}')
#         elif item['status'] == 'unchanged':
#             result.append(f'{SPACES*depth}  {item['key']}: {item['value']}')
#         elif item['status'] == 'changed':
#             result.append(f'{SPACES*depth}{MINUS}{item['key']}: {item['old value']}')
#             result.append(f'{SPACES*depth}{PLUS}{item['key']}: {item['new value']}')
#
#     result.append('{}}}'.format(SPACES * depth))
#
#     json_data = json.dumps(result, indent=4)
#     print(json_data)
#     return json_data


def stylish_formatter(diff):
    return '\n'.join(s_formatter(diff))
