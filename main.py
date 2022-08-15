import utils.json_utils as json_utils
from models.human import Human

if __name__ == '__main__':
    path = "jsons/"
    humans = json_utils.get_content(path)
    human0 = Human(**humans[0])
    print(human0)
    json_utils.write_entity_to_file('result_jsons/human0.json', human0)

    human1 = Human(name='name', surname='surname', age=1, phone_number=["+375333558361"],
                   address=[{'country': 'Belarus',
                             'city': 'Brest',
                             'street': 'Lenina',
                             'house': 2,
                             'letter': 'A',
                             'index': '111-222'}])
    json_utils.write_entity_to_file('result_jsons/human1.json', human1)

    new_address_for_human1 = Human.Address(country='Russia', city='Moscow', street='Red Place', house=1, letter='A',
                                           index='111-222')
    new_addresses_for_human1 = [new_address_for_human1, new_address_for_human1]
    human1.address = new_addresses_for_human1
    json_utils.write_entity_to_file('result_jsons/human1_updated_address.json', human1)

    human2 = human1
    human2._update_fields({'name': "New name", 'age': 99999})
    json_utils.write_entity_to_file('result_jsons/human2.json', human2)

    all_humans = [human0, human1, human2]
    json_utils.write_entity_to_file('result_jsons/all_humans.json', all_humans)
