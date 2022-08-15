class Human:
    """
    Business-model class for working with the "Person" entity
    """
    NAME_FIELD = 'name'
    SURNAME_FIELD = 'surname'
    AGE_FIELD = 'age'
    PHONE_NUMBER_FIELD = 'phone_number'
    ADDRESS_FIELDS = 'address'

    def __init__(self, **kwargs):
        """
        Initializer of Human entity object
        :param kwargs: dictionary with information about Human - name(str), surname(str), age(int),
        phone_number(list((str)) and address(list(dict))
        """
        self.name = kwargs.get(self.NAME_FIELD)
        self.surname = kwargs.get(self.SURNAME_FIELD)
        self.age = kwargs.get(self.AGE_FIELD)
        self.phone_number = kwargs.get(self.PHONE_NUMBER_FIELD)
        self.address = kwargs.get(self.ADDRESS_FIELDS)

    def _update_fields(self, data: dict):
        """
        Method to update all fields
        :param data: dictionary with Human entity fields and new values
        :return: None
        """
        self.name = data.get(self.NAME_FIELD, self.name)
        self.surname = data.get(self.SURNAME_FIELD, self.surname)
        self.age = data.get(self.AGE_FIELD, self.age)
        self.phone_number = data.get(self.PHONE_NUMBER_FIELD, self.phone_number)
        self.address = data.get(self.ADDRESS_FIELDS, self.address)

    def __repr__(self):
        return f"Name = {self.name}, " \
               f"Surname = {self.surname}, " \
               f"Age = {self.age}, " \
               f"Phone number = {self.phone_number}, " \
               f"Address = {self.address}"

    def to_json(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "phone_number": self.phone_number,
            "address": self.address
        }

    class Address:
        """
        Internal class for the "Address" structure
        """
        COUNTRY_FIELD = 'country'
        CITY_FIELD = 'city'
        STREET_FIELD = 'street'
        HOUSE_FIELD = 'house'
        LETTER_FIELD = 'letter'
        INDEX_FIELD = 'index'

        def __init__(self, **kwargs):
            """
            Initializer of Human Address field
            :param kwargs: dictionary with information about Address - country(str), city(str), street(str),
            house(int), letter(str), index(str)
            """
            self.country = kwargs.get(self.COUNTRY_FIELD)
            self.city = kwargs.get(self.CITY_FIELD)
            self.street = kwargs.get(self.STREET_FIELD)
            self.house = kwargs.get(self.HOUSE_FIELD)
            self.letter = kwargs.get(self.LETTER_FIELD)
            self.index = kwargs.get(self.INDEX_FIELD)

        def _upgrade_fields(self, data: dict):
            """
            Method to update all fields
            :param data: dictionary with Address fields and new values
            :return: None
            """
            self.country = data.get(self.COUNTRY_FIELD, self.country)
            self.city = data.get(self.CITY_FIELD, self.city)
            self.street = data.get(self.STREET_FIELD, self.street)
            self.house = data.get(self.HOUSE_FIELD, self.house)
            self.letter = data.get(self.LETTER_FIELD, self.letter)

        def __repr__(self):
            return f"[Country - {self.country}, " \
                   f"City - {self.city}, " \
                   f"Street - {self.street}, " \
                   f"House - {self.house}, " \
                   f"Letter - {self.letter}, " \
                   f"Index - {self.index}]"

        def to_json(self):
            return [{
                "country": self.country,
                "city": self.city,
                "street": self.street,
                "house": self.house,
                "letter": self.letter,
                "index": self.index
            }]
