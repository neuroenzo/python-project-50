import json


def build_raw_json(source):
    return json.dumps(source, indent=4)
