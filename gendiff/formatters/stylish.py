SEPARATOR = ' '
PLUS = '+ '
MINUS = '- '


def get_indent(indent, depth, status=None):
    match status:
        case 'nested' | 'unchanged':
            return SEPARATOR * indent * depth
        case 'added' | 'deleted' | 'changed':
            return SEPARATOR * 2 * (indent * depth - 1)
        case _:
            return SEPARATOR * 2 * indent * (depth - 1)


def build_stylish(source, depth=1):
    result = ['{']
    for item in source:
        match item['status']:
            case 'nested':
                result.append(
                    f"{get_indent(4, depth, item['status'])}{item['key']}:"
                    f" {build_stylish(item['value'], depth + 1)}"
                )
            case 'added':
                result.append(
                    f"{get_indent(2, depth, item['status'])}"
                    f"{PLUS}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'deleted':
                result.append(
                    f"{get_indent(2, depth, item['status'])}"
                    f"{MINUS}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'unchanged':
                result.append(
                    f"{get_indent(4, depth, item['status'])}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'changed':
                result.append(
                    f"{get_indent(2, depth, item['status'])}"
                    f"{MINUS}{item['key']}:"
                    f" {display_like_json(item['old value'], depth + 1)}"
                )
                result.append(
                    f"{get_indent(2, depth, item['status'])}"
                    f"{PLUS}{item['key']}:"
                    f" {display_like_json(item['new value'], depth + 1)}"
                )

    result.append(f'{get_indent(2, depth)}}}')

    return '\n'.join(result)


def display_like_json(structure, depth):
    match structure:
        case bool():
            return str(structure).lower()
        case None:
            return 'null'
        case dict():
            result = ['{']
            for key, value in structure.items():
                result.append(
                    f'{SEPARATOR * 4 * depth}{key}:'
                    f' {display_like_json(value, depth + 1)}'
                )
            result.append(f'{SEPARATOR * 4 * (depth - 1)}}}')
            return '\n'.join(result)
        case _:
            return structure
