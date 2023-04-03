import json


def create_json(info, path_to_file):
    with open(path_to_file, 'w') as f:
        json.dump(info, f, indent=4)
