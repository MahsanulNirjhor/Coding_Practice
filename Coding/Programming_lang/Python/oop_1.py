# Class
class Employee:
    #Construcotr
    def __init__(self,first,last):
        self.first = first
        self.last = last 
        # self.email = self.first + "." + self.last + "@company.com"
    def return_email(self):
        return f"{self.first}.{self.last}@company.com"
    def __str__(self) -> str:
        return f"Employee name is {self.first} {self.last}"
    def __repr__(self) -> str:
        return f"Employee({self.first},{self.last})"
    @classmethod
    def from_string(cls,name) -> str:
        return cls(name,"Pramanik")
    @staticmethod
    def multiply(x,y) -> int:
        return x*y
    
class Experience:
    def __init__(self, years):
        self.years = years
    def __str__(self):
        return self.years
    def __repr__(self) -> int:
        return self.years
class Developer(Employee,Experience):
    def __init__(self, first, last, years, title):
        Employee.__init__(self,first, last)
        Experience.__init__(self,years)
        self.title = title

    def __str__(self) -> str:
        emp_first = self.first
        emp_last = self.last
        emp_exp = self.years
        emp_title = self.title
        # return super().__str__()
        return f"Developer({emp_first},{emp_last},{emp_exp},{emp_title})"
    # pass


class Role(Employee):
    def __init__(self, first, last, role):
        super().__init__(first, last)
        self.role = role
    def __str__(self) -> str:
        return super().__str__()
    
import time

#--------------------- Test Case 5 -------------------------
emp_1 = Developer("Islam","Pramanik",1.5,"Backend Engineer")

start = time.time()
print(emp_1.return_email())
end = time.time()
runTime = end - start
print(f"Run Time :: {runTime}")

#--------------------- Test Case 5 -------------------------

#--------------------- Test Case 4 -------------------------
# emp_1 = Developer("Islam","Pramanik",1.5,"Backend Engineer")

# print(emp_1.__dict__)
# start = time.time()
# print(emp_1.__dict__)
# end = time.time()
# print(f'Run Time :: {end - start}')
# print(emp_1)
#--------------------- Test Case 4 -------------------------

#--------------------- Test Case 3 -------------------------

#--------------------- Test Case 3 -------------------------
# emp_1 = Role("Islam","Pramanik","Developer")
# print(emp_1)
# print(emp_1.__dict__)
# print(emp_1.role)
#--------------------- Test Case 3 -------------------------

#--------------------- Test Case 2 -------------------------

# emp_1=Employee("John","Smith")
# print(emp_1)
# # print(emp_1.email)
# print(emp_1.return_email())
# emp_1.first = "Doe"
# print(emp_1.first)
# print(emp_1)
# # print(emp_1.email)
# print(emp_1.return_email())
# print(emp_1.__dict__)

#--------------------- Test Case 2 -------------------------

#--------------------- Test Case 1 -------------------------
# emp_1=Employee("John","Smith")
# print(emp_1)
# emp_2 = Employee.from_string("Islam")
# print(emp_2)
# print(Employee.multiply(10,12))
#--------------------- Test Case 1 -------------------------