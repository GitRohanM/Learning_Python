#example
#Recursive function
def show(n):
    if(n == 0):             #Base case
        return
    print(n)
    show(n-1)               #Recursion


# Questions

# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n == 1):
        return 1

    return n + sum(n-1)

print(sum(5))


# Write a recursive function to print all elements in a list
nums = [1, 4, 9, 16, 36]  # List
def print_list(nums, index):
    if(index == len(nums)):
        return
    
    print(nums[index])
    print_list(nums,index+1)

print_list(nums,0)
