import json
import os

FILE_EXTENSION = '.json'


def default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


def write_entity_to_file(filepath, entity):
    with open(filepath, 'w') as json_file:
        json.dump(entity, json_file, default=default, indent=2)


def __get_file_contents(file_name, extension):
    if file_name.endswith(extension):
        with open(file_name, 'r') as f:
            file_contents = json.load(f)
        return file_contents


def get_content(path):
    contents = []
    if os.path.isdir(path):
        for file in os.listdir(path):
            contents.append(__get_file_contents(path + file, FILE_EXTENSION))
        return contents
    elif os.path.isfile(path):
        contents.append(__get_file_contents(path, FILE_EXTENSION))
        return contents
    else:
        raise f"{path} is not a directory or a file"
