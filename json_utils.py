import os
import json

from json_models.human import Human


def set_human(json_file_contents):
    human = Human(json_file_contents["name"],
                  json_file_contents["surname"],
                  json_file_contents["age"],
                  json_file_contents["phone_number"],
                  json_file_contents["address"])
    return human


def json_to_python(json_files_contents):
    if type(json_files_contents) is list:
        humans = []
        for json_file_contents in json_files_contents:
            if type(json_file_contents) is list:
                for item in json_file_contents:
                    humans.append(set_human(item))
            elif type(json_file_contents) is dict:
                humans.append(set_human(json_file_contents))
        return humans

    elif type(json_files_contents) is dict:
        human = set_human(json_files_contents)
        return human


def get_json_files_contents(path):
    extension = ".json"

    if os.path.isdir(path):
        json_files_contents = []
        for file in os.listdir(path):
            if file.endswith(extension):
                with open(os.path.join(path, file), 'r') as json_file:
                    json_file_contents = json.load(json_file)
                json_files_contents.append(json_file_contents)
        if len(json_files_contents) > 1:
            return json_files_contents
        elif len(json_files_contents) == 1:
            return json_files_contents[0]
        else:
            print(f"There are no '{extension}' files in the '{path}' folder!")

    elif os.path.isfile(path):
        if path.endswith(extension):
            with open(os.path.join(path), 'r') as json_file:
                json_file_contents = json.load(json_file)
                return json_file_contents
        else:
            print(f"The file '{path}' does not have the '{extension}' extension")
    else:
        print(f"File '{path}' not found!")
