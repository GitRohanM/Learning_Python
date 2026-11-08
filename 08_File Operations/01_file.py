# Create a new file "practice.txt" using python. Add some text to it
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using python\n")
    f.write("I like programming in python.")


# WAF that replaces occurence of "Java" with "python" in above file
# First Read and then overwrite
with open("practice.txt", "r") as f:
    data = f.read()

newData = data.replace("python", "java")

with open("practice.txt", "w") as f:
    f.write(newData)

# Search if the word "learning" exists in the file or not
def check_for_word():     
    with open("practice.txt", "r") as f:
        data = f.read()
        word = "learning"
        if (data.find(word) != -1):
            print("Found!")
        else:
            print("Not Found!")

# WAF in which line of the file does the word "learning" occur first. Print -1 if not found

def check_line_number():
    word = "learning"
    data = True
    lineNo = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                return lineNo
            lineNo += 1
    return -1

print(check_line_number())


# From a file containing numbers separated by comma, print the count of even numbers.

# 1. Manually 
def print_even_count():
    count = 0
    with open("08_File Operations/nums.txt", "r") as f:
        data = f.read()

        num = ""
        for i in range(len(data)):
            if data[i] == ",":
                if int(num) % 2 == 0:
                    count += 1
                num = ""
            else:
                num += data[i]

    print(count)
print_even_count()



# 2. Using split() function - built in function
def print_even_count2():
    count = 0
    with open ("08_File Operations/nums.txt", "r") as f:
        data = f.read()
        print(data)

        nums = data.split(",")
        for val in nums:
            if (int(val) % 2 == 0):
                count += 1

    print(count)

print_even_count2()