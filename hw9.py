from collections import UserDict

class Field:
    """Base class for fields in record"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for name in record"""
    pass


class Phone(Field):
    """Class for phone number in record"""
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone must be in a string format")
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone must be 10 digit string format")

        self.value = value


class Record:
    """Class for record in address book"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, phone: str, new_phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            self.phones.append(Phone(new_phone))

    def find_phone(self, phone: str):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj


class AddressBook(UserDict):
    """Class for address book"""
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data.keys():
            return self.data[name]

    def delete(self, name: str):
        if self.find(name):
            del self.data[name]
