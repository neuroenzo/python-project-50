import json
import yaml

from pathlib import Path

from gendiff.formats import build_formatter


def define_file_type(file_name):
    with open(file_name) as f:
        data = f.read()
    match Path(file_name).suffix:
        case '.json':
            return json.loads(data)
        case '.yml' | '.yaml':
            return yaml.safe_load(data)
