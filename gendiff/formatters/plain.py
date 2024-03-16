def plain_formatter(source, path=None):
    if path is None:
        path = ()
    result = []
    for item in source:
        status = item['status']
        bread_crumbs_path = path + (item['key'], )
        if status == 'nested':
            result.append(
                plain_formatter(item['value'], bread_crumbs_path)
            )
        elif status == 'added':
            result.append(
                f"Property '{correct_plain_conclusion(bread_crumbs_path)}'"
                f" was added with value:"
                f" {correct_plain(item['value'])}"
            )
        elif status == 'deleted':
            result.append(
                f"Property '{correct_plain_conclusion(bread_crumbs_path)}'"
                f" was removed")
        elif status == 'changed':
            result.append(
                f"Property '{correct_plain_conclusion(bread_crumbs_path)}'"
                f" was updated."
                f" From {correct_plain(item['old value'])}"
                f" to {correct_plain(item['new value'])}"
            )

    return '\n'.join(result)


def correct_plain_conclusion(bread_crumbs_path):
    return '.'.join(bread_crumbs_path)


def correct_plain(structure):
    match structure:
        case bool():
            return str(structure).lower()
        case dict():
            return '[complex value]'
        case str():
            return f"'{structure}'"
        case None:
            return 'null'
        case _:
            return structure
