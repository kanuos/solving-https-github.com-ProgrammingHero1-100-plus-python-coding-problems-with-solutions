# Password generator with requirements
# Generate a password that has a minimum of one uppercase, one lowercase,
# one digit, and one special character

import random
from string import digits, ascii_lowercase, ascii_uppercase, punctuation

try:
    print("WELCOME TO PASSWORD GENERATOR  :")
    length = int(input("Enter the password length : "))
    if length <= 4:
        raise ValueError("Password cannot be less than 5 characters long")
    space = list(digits + ascii_lowercase + ascii_uppercase + punctuation)
    uppercase = False
    lowercase = False
    digit = False
    special = False
    while not (uppercase or lowercase or digit or special):
        random.shuffle(x=space)
        space = random.choices(space, k=length)
        for c in space:
            if c.isalpha() and c.islower():
                lowercase = True
            elif c.isalpha() and c.isupper():
                uppercase = True
            elif c.isdigit():
                digit = True
            elif c in ['+', '-', '_', '/', '@', '$']:
                special = True
    print("Password : ", "".join(space))
except ValueError as e:
    print(e)
