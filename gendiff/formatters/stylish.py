INDENTS = '  '
PLUS = '+ '
MINUS = '- '


def stylish_formatter(source, depth=1):
    result = ['{']
    for item in source:
        match item['status']:
            case 'nested':
                result.append(
                    f"{INDENTS*2*depth}{item['key']}:"
                    f" {stylish_formatter(item['value'], depth+1)}"
                )
            case 'added':
                result.append(
                    f"{INDENTS*(2*depth-1)}{PLUS}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'deleted':
                result.append(
                    f"{INDENTS*(2*depth-1)}{MINUS}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'unchanged':
                result.append(
                    f"{INDENTS*2*depth}{item['key']}:"
                    f" {display_like_json(item['value'], depth + 1)}"
                )
            case 'changed':
                result.append(
                    f"{INDENTS*(2*depth-1)}{MINUS}{item['key']}:"
                    f" {display_like_json(item['old value'], depth + 1)}"
                )
                result.append(
                    f"{INDENTS*(2*depth-1)}{PLUS}{item['key']}:"
                    f" {display_like_json(item['new value'], depth + 1)}"
                )
    result.append(f'{INDENTS*2*(depth-1)}}}')

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
                    f'{INDENTS*2*depth}{key}:'
                    f' {display_like_json(value, depth + 1)}'
                )
            result.append(f'{INDENTS*2*(depth-1)}}}')
            return '\n'.join(result)
        case _:
            return structure
