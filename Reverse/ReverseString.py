# Reverse a string
# If the input is: Hello World.
# The output should be: .dlroW olleH

def reverse_string(string):
    return string[::-1]


try:
    s = input("Input : ")
    print("The output : " + reverse_string(s))
except ValueError:
    print("Invalid input")
