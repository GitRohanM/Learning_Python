# # Each element in set is unique and immutable
# # We can store List and Dictionary type in set because they are mutable

# #creation of set
# set1 = {1,2,3,4}
# print(type(set1))

# set2 = {1,2,1,2} # Duplicate elements are stored only once, so it resolved to {1,2}
# print(set2)

# # Creation of Empty Set
# null_set = set()
# print(type(null_set))
# null_set2 = {} # This is a syntax of empty dictionary

# # Set Methods
# set1.add(5) # Adds an element
# set1.remove(2) # Removes an element
# set1.clear() # Empties the set
# set1.pop() # removes a random value

# print(set1)

## ----------------------Note------------------------- 
## Set is Mutable means you can add or remove elements
## Set elements are immutable means you cant change them

# Unique Methods
set3 = {1,2}
set4 = {4,5,1,2}
print(set3.union(set4))  # Combines both set values & returns new
print(set3.intersection(set4))  # Combines common values & returns new