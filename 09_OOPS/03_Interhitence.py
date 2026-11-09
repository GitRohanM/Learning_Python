# Basic Example - Single Inheritance

class Car:
    color = "Black"
    __model = 2018      #   Private attribute (__) 

    @staticmethod
    def get_model():
        print(Car.__model)


class ToyotaCar(Car):   # Inheritance
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

car1.get_model()


# Example - Multi Level Inheritance

class Car:
    color = "Black"
    __model = 2018      

    @staticmethod
    def get_model():
        print(Car.__model)


class ToyotaCar(Car):   
    def __init__(self, brand):
        self.brand = brand

class FortunerCar(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = FortunerCar("Diesel")
car1.get_model()


# Example - Multiple Inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)


# Super() method - Common use is to call the constructor of the parent class from the child class.
class Car:
    color = "Black"
    __model = 2018      #   Private attribute (__) 

    def __init__(self, type):
        self.type = type
        print("Parent class constructor called")

    @staticmethod
    def get_model():
        print(Car.__model)


class ToyotaCar(Car):   # Inheritance
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)




car1 = ToyotaCar("fortuner", "SUV")
car2 = ToyotaCar("prius", "Hatchback")
print(car1.type)


# Example - overwriting value of parent class variable in child class
class Person:
    name = "Anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
print(p1.name)
p1.changeName("John")
print(p1.name)


# Example - @property decorator
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property           # This decorator automatically reflect changes and update values
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"

s1 = Student(98,97,92)
print(s1.percentage)

s1.phy = 100
s1.chem = 100
s1.maths = 100
print(s1.percentage)