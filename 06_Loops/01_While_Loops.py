# while True:
#     #code block to be executed repeatedly


#Practice Questions:

# WAP to print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1


# WAP to print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


# WAP to print multiplication table of n
n = 12
i =  1
while i <= 10:
    print(n * i)
    i += 1


# WAP to print the elements of a list 
nums = [1, 4 , 9, 16, 25, 36, 49, 64, 81, 100]  # List
i = 1 # iterator
while i < len(nums):
    print(nums[i])
    i += 1


# WAP to search a number x in a tuple
nums1 = (1, 4 , 9, 16, 25, 36, 49, 64, 81, 100)  # Tuple
i = 1 # Iterator
x = 35  # Target Element
while i < len(nums1):
    if(nums1[i] == x):
        print("Element found!")   
        break; # Come out from the loop 
    i += 1
else:
    print("Element not found!") # Optional which runs after loop completion