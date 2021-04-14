# Cows and Bulls (2 digits)
# The Problem
# Create a Cows and Bulls game with 2 digit numbers.
from CreateRandomList import create_random_list

lower_limit = 0
upper_limit = 9

try:
    bull = 0
    cow = 0
    pc = create_random_list(2)
    print("Cows and bulls game.\n PC has guessed a two digit number. Start guessing..")
    user = [int(input("Enter the first digit : ")), int(input("Enter the second digit : "))]
    for i, cur in enumerate(pc):
        if cur in user:
            if user.index(cur) == i:
                bull += 1
            else:
                cow += 1
    print(f"Result : {bull} bulls and {cow} cows")
    print("PC guessed  : ", str(pc))
    print("You guessed : ", str(user))
except ValueError:
    print("Inputs must be numbers")
