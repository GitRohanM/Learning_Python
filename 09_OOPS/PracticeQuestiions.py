"""
Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle. 
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius * self.radius

    def Perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(5)
print(f"Area of Circle: {c1.Area():.2f}")
print(f"Perimeter of Circle: {c1.Perimeter():.2f}")  

#-------------------------------------------------------------------------------------------------------------------

"""
Define a Employee class with attributes role, department & salary. This class also have a showDetails() method.
Create a Engineer class that inherits properties from Employee & has additional attributes: name & age
"""

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def ShowDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT", "75,000")

e1 = Engineer("Rohan", 24)

e1.ShowDetails()


#---------------------------------------------------------------------------------------------------------------------------

"""
Create a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that: 
order1 > order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price


order1 = Order("Laptop", 100000)
order2 = Order("Iphone", 150000)

price_Check = order2 > order1
print(price_Check)