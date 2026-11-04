# Three types of creating strings in Python
str1 = "This is a string"
str2 = 'This is also a string'
str3 = """This is a string""" 

# escape characters
str4 = "This is a string with a newline\ncharacter"
print(str4)
str5 = "This is a string with a tab\tcharacter"
print(str5)

# Basic Operations
# 1. Concatenation
str6 = "Rohan"
str7 = "Manav"
concat_str = str6 + " " + str7
print(concat_str)

# 2. Length
print(len(concat_str))

# Accessing char
print(concat_str[0])

# Slicing
print(concat_str[0:3]) # Last index is always excluded
print(concat_str[0:len(concat_str)])
