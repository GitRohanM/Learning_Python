# Polymorphism - Operator Overloading

# Simple built-in python example
print(1 + 2) #3
print("Rohan" + "Manav") #RohanManav
print([1, 2, 3] + [4, 5, 6]) #[1, 2, 3, 4, 5, 6] 
# All the above examples are using the same operator '+' but performing different operations based on the data type of the operands.

# Custom example of sum of Complex Numbers
# 2i + 2j - num1
# 4i + 6j - num2
# 6i + 8j - Sum of num1 and num2 (what we want to achieve)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(self.real,"i", + self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

no1 = Complex(2,2)
no1.ShowNumber()

no2 = Complex(4,6)
no2.ShowNumber()

sum = no1.add(no2)
sum.ShowNumber()


# Same Custom example of sum of Complex Numbers using dunder functions

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(self.real,"i", + self.img, "j")

    def __add__(self, num2):            #   Addition dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):            #   Subtraction dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

no1 = Complex(2,2)
no1.ShowNumber()

no2 = Complex(4,6)
no2.ShowNumber()

sum = no1 + no2     # now you can use '+' operator
sum.ShowNumber()

sub = no1 - no2     # now you can use '-' operator
sub.ShowNumber()