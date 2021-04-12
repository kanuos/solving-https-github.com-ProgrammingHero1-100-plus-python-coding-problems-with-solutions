# Reverse a string using stack
# If the input is: Hello World.
# The output should be: .dlroW olleH

try:
    string = list(input("Enter the string : "))
    reverse_list = []
    while len(string) > 0:
        reverse_list.append(string.pop())
    print("".join(reverse_list))

except ValueError:
    print("Invalid Input")
