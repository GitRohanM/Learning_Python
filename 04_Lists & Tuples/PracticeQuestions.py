#WAP to ask the user to enter names of their 3 fav movies & store them in a list.

list = []
list.append(input("Enter first movie: "))
list.append(input("Enter second movie: "))
list.append(input("Enter third movie: "))

print(list)

#WAP to check if a list contains a palindrome of elements
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")


#WAP to count the no. of students with the "A" grade in the following tuple
tup = ("C", "D", "A", "A", "B", "B", "A")
print("Count of students who scored 'A' Grade is:", tup.count("A"))

#Store same grades in a list and sort them in ascending order
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)