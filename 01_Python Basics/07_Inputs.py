# input()

# name = input("Enter your name: ")
# print("Welcome,", name)

# input from user is always treated as a string
num1 = input("Enter a number: ")
print("Type:", type(num1)) # Str type

# So to get a no. as input, we have to type cast it
num2 = int(input("Enter a number: "))
print("Type:", type(num2)) # Int type