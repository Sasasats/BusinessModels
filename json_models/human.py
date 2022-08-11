import json


class Human:
    def __init__(self, name: str, surname: str, age: int, phone_number=None, address=None):
        self.__name = name if type(name) is str else None
        self.__surname = surname if type(surname) is str else None
        self.__age = age if type(age) is int else None
        self.__phone_number = phone_number if type(phone_number) is str or type(phone_number) is list else None
        self.__address = address if type(address) is dict or type(address) is list or type(
            address) is Human.Address else None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            print(f"Invalid data type {type(name)}")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) is str:
            self.__surname = surname
        else:
            print(f"Invalid data type {type(surname)}")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            print(f"Invalid data type {type(age)}")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if type(phone_number) is str or type(phone_number) is list:
            self.__phone_number = phone_number
        else:
            print(f"Invalid data type {type(phone_number)}")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) is Human.Address:
            self.__address = dict(address)
        elif type(address) is dict or type(address) is list:
            self.__address = address
        else:
            self.__address = None

    def __str__(self):
        return json.dumps(self.to_json())

    def to_json(self):
        address = self.__address
        if type(self.__address) is Human.Address:
            address = self.__address.to_json()
        to_return = {"name": self.__name,
                     "surname": self.surname,
                     "age": self.age,
                     "phone_number": self.phone_number,
                     "address": address}
        return to_return

    class Address:
        def __init__(self, country: str = None, city: str = None, street: str = None, house: int = None,
                     letter: str = None, index: str = None):
            self.__country = country if type(country) is str else None
            self.__city = city if type(city) is str else None
            self.__street = street if type(street) is str else None
            self.__house = house if type(house) is int else None
            self.__letter = letter if type(letter) is str else None
            self.__index = index if type(index) is str else None

        @property
        def country(self):
            return self.__country

        @country.setter
        def country(self, country):
            if type(country) is str:
                self.__country = country
            else:
                print(f"Invalid data type {type(country)}")

        @property
        def city(self):
            return self.__city

        @city.setter
        def city(self, city):
            if type(city) is str:
                self.__city = city
            else:
                print(f"Invalid data type {type(city)}")

        @property
        def street(self):
            return self.__street

        @street.setter
        def street(self, street):
            if type(street) is str:
                self.__street = street
            else:
                print(f"Invalid data type {type(street)}")

        @property
        def house(self):
            return self.__house

        @house.setter
        def house(self, house):
            if type(house) is int:
                self.__house = house
            else:
                print(f"Invalid data type {type(house)}")

        @property
        def letter(self):
            return self.__letter

        @letter.setter
        def letter(self, letter):
            if type(letter) is str:
                self.__letter = letter
            else:
                print(f"Invalid data type {type(letter)}")

        @property
        def index(self):
            return self.__index

        @index.setter
        def index(self, index):
            if type(index) is str:
                self.__index = index
            else:
                print(f"Invalid data type {type(index)}")

        def __str__(self):
            return json.dumps(dict(self), ensure_ascii=True)

        def to_json(self):
            to_return = {"country": self.__country,
                         "city": self.__city,
                         "street": self.__street,
                         "house": self.__house,
                         "letter": self.__letter,
                         "index": self.__index}
            return to_return
