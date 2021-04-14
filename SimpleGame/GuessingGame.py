# Guessing Game
# The Problem
# Build a simple guessing game where it will continuously ask the user to enter a
# number between 1 and 10.
#
# If the user's guesses matched, the user will score 10 points, and display the score.
# If the users' guess does not match display the generated number.
#
# Also, if the user enters “q” then stop the game.
import random

try:
    print("Guessing Game.. guess any number between 1 to 10")
    pc = random.randint(1, 10)
    count = 0
    while True:
        user = int(input("Guess the number (1-10) : "))
        if user > 10 or user < 1:
            raise ValueError("You are supposed to guess between 1 and 10.")
        count += 1
        if pc == user:
            print(f"Bingo! You guessed it correctly in {count} attempts. Your score : {10 - count}/")
            break
        else:
            if user > pc:
                print("You are guessing higher..")
            else:
                print("You are guessing lower..")
            q = input("Do you want to quit? Press 'q' to quit...").lower()
            if q == "q":
                break
except ValueError as err:
    print(err)
