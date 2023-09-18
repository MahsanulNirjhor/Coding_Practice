# from typing import Any
class Person:
    def __init__(self, name, age):
        self.name = name
        # To declare private attribute you have to add "__" prefix
        self.__age = age

    @property
    def change_age(self):
        return self.__age
    @change_age.setter
    def change_age(self,age):
        self.new_age = age
        self.__age = self.new_age

    def __setattr__(self, key: str, value: any) -> None:
        if key == "new_age":
            print(f"Setting the {key} attribute to {value}")
        elif key == "name":
            print(f"Setting the {key} attribute to {value}")
        super().__setattr__(key, value)

    def __delattr__(self, __key: str) -> None:
        if __key == "name":
            raise AttributeError("Can't delete name")
        pass
        

person = Person("Alice", 20)
print(person.__dict__)


person.change_age = 30
person.name = "Bob" 
print(person._Person__age)

# print(person.__dict__)

del person.new_age
print(person.__dict__)

try:
    del person.name
except AttributeError:
    print("Can't delete name directly.")
