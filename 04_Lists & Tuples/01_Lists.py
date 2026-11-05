marks = [85.4, 90.5, 78.0, 92.0, 88.5]
marks[0] = "Rohan"
print(marks)
print(type(marks))
print(len(marks))

#Strings are immutable
#Lists are mutable

# List Slicing
print(marks[1:4])  # Slicing from index 1 to 3

#List Methods
list = [2,1,4,3,1]

list.append(5) # Adds element at the end of list
list.sort() # Sorts in ascending order
list.sort(reverse=True) # Sorts in descending order
list.reverse() # Reverses the list
list.insert(1, 5) # Inserts element at specific index
list.remove(1) # Removes the first occurence of the element
list.pop(1) # Removes element at index

print(list)