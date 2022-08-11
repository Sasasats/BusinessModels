import json
import json_utils
from json_models.human import Human


def default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


def write_entity_to_file(filepath, entity):
    with open(filepath, 'w') as json_file:
        json.dump(entity, json_file, default=default, indent=2)


if __name__ == '__main__':
    json_files = json_utils.get_json_files_contents("/home/asats/PycharmProjects/BusinessModels/jsons/")
    humans = json_utils.json_to_python(json_files)
    write_entity_to_file("json_results/result.json", humans)

    human1 = Human("name", "surname", 12, "+375291112233",
                   Human.Address("Belarus", "Brest", "Lenina", 1, "A", "111-222"))

    address = Human.Address()
    address.country = "haha"
    address.city = "hoho"
    address.street = "hehe"
    address.house = 12
    address.letter = "X"
    address.index = "123-456"

    human2 = Human("name2", "surname2", 22)
    human2.phone_number = ["375291112233", "+375331112233"]
    human2.address = [address, address]

    humans12 = [human1, human2]
    write_entity_to_file("json_results/humans12.json", humans12)
