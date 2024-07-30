import json
import yaml

from pathlib import Path

from utils.custom_exceptions import FileFormatError


def get_data(path_to_file):
    format_name = Path(path_to_file).suffix
    with open(path_to_file) as f:
        data = f.read()
        return parse_data(data, format_name)


def parse_data(data, format_name):
    match format_name:
        case '.json':
            return json.loads(data)
        case '.yml' | '.yaml':
            return yaml.safe_load(data)
    raise FileFormatError(f'{format_name} is not available format')
