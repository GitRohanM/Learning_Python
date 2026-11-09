# Create a Student class that takes name and marks of 3 subjects as arguements in constructor.
# Then create a method to print the average

class Student:                          #   Class
    college_name = "ABC"                #   Class Attributes
    def __init__ (self, name, marks):   #   Constructor
        self.name = name                #   Object Attributes
        self.marks = marks

    def find_average(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hi", self.name,"your avg score is:", sum/len(self.marks))


s1 = Student("Rohan", [84, 97, 92])     #   Object
s1.find_average()

s1.name = "Manav"
s1.find_average()