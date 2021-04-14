# Cows and Bulls
# The Problem
# Create a Cows and Bulls game with a 4 letter word.
from GetEnglishDictionary import generate_four_letter_words
import random

lower_limit = 0
upper_limit = 9

try:
    bull = 0
    cow = 0
    pc = random.choice(generate_four_letter_words())
    print("Cows and bulls game.\n PC has guessed a four letter word. Start guessing..")
    user = input("Your guess : ")
    if len(user) != len(pc):
        raise ValueError("You are supposed to guess a four letter word")
    for i, cur in enumerate(pc):
        if cur in user:
            if user.index(cur) == i:
                bull += 1
            else:
                cow += 1
    print(f"Result : {bull} bulls and {cow} cows")
    print("PC guessed  : ", pc)
    print("You guessed : ", user)
except ValueError as err:
    print(err)
