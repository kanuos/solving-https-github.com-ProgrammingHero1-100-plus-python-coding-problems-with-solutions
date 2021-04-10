# Remove duplicate characters
# The problem
# For a given string, remove all duplicate characters from that string.

try:
    string = input("Enter the string : ")
    print(string)
    if len(string) == 0:
        raise ValueError("Empty string entered")
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    print("".join(unique_chars))

except ValueError as err:
    print(err)
