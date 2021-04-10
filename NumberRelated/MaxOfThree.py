# max of three
# The problem
# Find the max number of three numbers.
#
# Hints
# Ask the user to enter two numbers.
# Then, you can run a comparison to compare which one is larger.

try:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    num3 = float(input("Enter the third number : "))

    if num1 == num2 == num3:
        print(f"{num1}, {num2}, {num3} are equal")
    elif num1 > num2:
        if num1 > num3:
            print(f"{num1} is the greatest of {num1}, {num2}, {num3}")
        else:
            print(f"{num3} is the greatest of {num1}, {num2}, {num3}")
    else:
        if num2 > num3:
            print(f"{num2} is the greatest of {num1}, {num2}, {num3}")
        else:
            print(f"{num3} is the greatest of {num1}, {num2}, {num3}")

except ValueError:
    print("Inputs must be numbers")
