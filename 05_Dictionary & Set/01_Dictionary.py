# key : value pairs
info = {
    "name" : "Rohan",
    "subjects" : ["Python", "C", "Java"],
    "age" : 24,
    "marks" : 94.4
}

print(type(info))
print(info["name"])  # Accesing value using key

info["name"] = "Manav"  # Modifying value using key
print(info)

info["email"] = "rohanxxxxxxx@gmail.com"  # Adding key with value
print(info)

null_dict = {}  # Creation of null dictionary
print(type(null_dict))

# Nested dictionary
student = {
    "name" : "Rohan Manav",
    "score" : {
        "c++" : 98,
        "python" : 97,
        "java" : 92
    },
    "cgpa" : 9.6
} 

print(student["score"]["java"]) # Accessing nested dictionary value using keys


# Dictionary Methods
print(student.keys())  # Returns all Keys

print(student.values())  # returns all values

print(student.items())  #  Returns all pairs as tuples

print(student.get("name"))  #  Returns the value of the key, but also returns NONE if wrong key is entered

print(student.update({"city" : "Jalandhar"}))  #  Inserts the specified items to the dictionary or overwrites existing values
print(student)