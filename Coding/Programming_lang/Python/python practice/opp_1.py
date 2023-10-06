#class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def email(self):
        self.email = self.name + str(self.age) +"@gmail.com"
        print(f'Email is {self.email}')

Nirjhor = Person("Nirjhor",29)
print(Nirjhor.name)
print(Nirjhor.age)  
Nirjhor.email()
