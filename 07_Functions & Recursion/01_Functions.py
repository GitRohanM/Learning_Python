# #syntax
# #def function_name(parameter1, parameter2):
# #    #body


# # Questions

# # WAP to print the length of a list
# nums = [1, 4, 9, 16, 36]
# def list_len(nums):
#     return len(nums)

# print(list_len(nums))


# # WAP to print the elements of a list in a single line
# def print_ele(nums):
#     for i in range(len(nums)):
#         print(i)

# print_ele(nums)


# WAP to find the factorial of n 
def factorial(n):
    result = 1

    for i in range (1,n+1):
        result *= i

    return result

print(factorial(5))


# WAP to convert USD to INR
def conversion(usd):
    result = usd * 96

    return result

print(conversion(100))