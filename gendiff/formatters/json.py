import json


def make_raw_json(source):
    return json.dumps(source, indent=4)
