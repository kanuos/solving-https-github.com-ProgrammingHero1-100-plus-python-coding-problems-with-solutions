# Check Palindrome

def is_palindrome(string):
    return string == string[::-1]


try:
    s = input("Enter the string : ")
    print(f"'{s}' {'is' if is_palindrome(s) else 'is not'} a palindrome string")
except ValueError:
    print("Invalid Input")
