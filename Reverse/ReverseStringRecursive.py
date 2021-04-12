# Reverse a string (recursion)
# The problem
# Reverse a string using a recursive function.

def reverse_recursive(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse_recursive(string[:-1])


try:
    s = input("Enter the string : ")
    print("The output : " + reverse_recursive(s))
except ValueError:
    print("Invalid input")
