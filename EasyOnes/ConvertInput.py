# The problem
# Take two inputs from the user. One will be an integer. The other will be a float number.
# Then multiply them to display the output.

try:
    integer = int(input("Enter an integer number : "))
    real = float(input("Enter a floating number : "))
    print(f"{integer} * {real} = {integer * real}")
except TypeError:
    print("Inputs must be a number")
except ValueError:
    print("Expected an integer and got a floating number")
