#for el in name:
    #code to be executed

# Practice Questions

# Print the elements of list using for loop
nums = [1, 4 , 9, 16, 25, 36, 49, 64, 81, 100]  # List
for num in nums:
    print(num)


# WAP to search a number x in a tuple
nums1 = (1, 4 , 9, 16, 25, 36, 49, 64, 81, 100)  # Tuple
x = 81                  # Target Element
idx = 0                 # To keep track of index
for el in nums1:
    if(el == x):
        print("Element found at index: ", idx)
    idx += 1


# range() function
# Default Start - 0, Default Increment - 1, Stops before specified number
# range(start?, stop, step?)

for i in range(5):      # range(stop)
    print(i)

for i in range(1,5):      # range(start, stop)
    print(i)

for i in range(2,10,2):      # range(start, stop, step)
    print(i)



# Practice Questions for range()

# Print 1 to 100
for i in range(1,101):
    print(i)


# Print 100 to 1
for i in range(100, 0, -1):
    print(i)


# Print Multiplication Table
n = 12
for i in range(1,11):
    print(i * n)


# pass statement

for i in range(10):
    pass   # Empty -> Just used as a placeholder for future code