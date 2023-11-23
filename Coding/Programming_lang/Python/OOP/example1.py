from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def make_sound(self):
        pass
    @abstractclassmethod
    def eyes(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!!")
    def eyes(self):
        print("Two")
class Cat(Animal):
    def make_sound(self):
        print("Meaw!!!")
    def eyes(self):
        pass

class Pet_Owner():
    def __init__(self,animal) -> None:
        self.animal = animal

    def make_pet_make_sount(self):
        self.animal.make_sound()


################# Inheriteance Check ###################
# dog = Dog()
# dog.make_sound()
################# Inheriteance Check ###################

################# Composition Check ###################

dog = Dog()
cat = Cat()

person_1 = Pet_Owner(dog)
person_2 = Pet_Owner(cat)

person_1.make_pet_make_sount()
person_2.make_pet_make_sount()

################# Composition Check ###################