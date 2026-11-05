# Tuples are immutable
tup = (2, 15 ,90)
tup2 = (1,) # Single element tuple; if we dont add comma at last python will treat it like normal data types(int, float, str) 
print(type(tup))

# Tuple Slicing
print(tup[1:3])

# Tuple Methods
tup.index(15) # Returns the index of the first occurrence of the specified value

tup.count(15) # Returns the number of times a specified value occurs in a tuple