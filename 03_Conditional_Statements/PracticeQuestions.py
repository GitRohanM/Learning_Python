# WAP to Grade students based on marks
marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Grade: A")
elif(marks >= 80 and marks < 90):
    print("Grade: B")
elif(marks >= 70 and marks < 80):
    print("Grade: C")
elif(marks < 70):
    print("Grade: D")


# WAP to check if a no. entered is odd or even
num = int(input("Enter a number to check a no. is odd or even: "))
if(num % 2 == 0):
    print("No. is Even")
else:
    print("No. is Odd")

# WAP to find the greatest of 3 no. entered by user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 >= num2 and num1 > num3):
    print("Greatest number is:", num1)
elif(num2 >= num3):
    print("Greatest number is:", num2)
else:
    print("Greatest number is:", num3)

# WAP to check if a no. is a multiple of 7 or not
num4 = int(input("Enter a number to check if it is a multiple of 7 or not: "))
if(num4 % 7 == 0):
    print("This number is a multiple of 7!")
else:
    print("This number is not a multiple of 7!")