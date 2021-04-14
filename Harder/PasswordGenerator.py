# Password generator
# Generate a password. Your password may contain letters in uppercase or lowercase.
# It also may contain digits or special characters.
#
# Hints
# To select a random character from a string, you can import random.
# Then use the random. choice method. This will select a character from the provided string.
#
# Also, you can import the string module.
#
# This is not just the string type variable. Instead, it has a lot of extra functionalities.
#
# For example, you can use string.ascii_letters to get all the characters a to z both in
# lowercase and upper case.
# Similarly, you can use string.digits to get all the single digits.
# Also, you can use string.punctuation to get all the special characters.

import random
from string import digits, ascii_lowercase, ascii_uppercase, punctuation

try:
    print("WELCOME TO PASSWORD GENERATOR  :")
    length = int(input("Enter the password length : "))
    space = list(digits + ascii_lowercase + ascii_uppercase + punctuation)
    random.shuffle(x=space)
    space = "".join(random.choices(space, k=length))
    print("Password generated : ", space)
except ValueError as e:
    print(e)
