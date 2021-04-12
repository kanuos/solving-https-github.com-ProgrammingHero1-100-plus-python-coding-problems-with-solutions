# Reverse word order
# For example, if the input string is “Hello young Programmer”,
# the output will be “Programmer young Hello”

def reverse_word(sentence: str):
    words = sentence.split(' ')
    output = []
    for word in words:
        output.append(word[::-1])
    return " ".join(output)


try:
    inp = input("Enter a string : ")
    print("Output : " + reverse_word(inp))
except ValueError:
    print("Invalid Input")
