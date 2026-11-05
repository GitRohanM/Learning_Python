# Store Words and their meaning in a dictionary
words = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

# Given a list of subjects for students. Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students.
classrooms = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("Total classrooms required are:", len(classrooms))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
student = {}

x = int(input("Maths: "))
student.update({"Maths" : x})

x = int(input("English: "))
student.update({"English" : x})

x = int(input("Hindi: "))
student.update({"Hindi" : x})

print(student)


# Figure out a way to store 9 & 9.0 as separate values in the set

set1 = {9, "9.0"}

set2 = {
    ("float", 9.0),
    ("int", 9)
}
print(set1)
print(set2)