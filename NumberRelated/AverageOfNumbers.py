# The problem
# Take numbers from a user and show the average of the numbers the user entered.

try:
    array = []
    total = 0
    while True:
        num = float(input(f"Enter the #{len(array) + 1} number : "))
        array.append(num)
        total += num
        keep_adding = input("Do you want to keep adding (yes/no)? ").lower()
        if keep_adding in ["no", "n"]:
            break
    avg = total / len(array)
    print(f"The average of {array} : {avg}")
except ValueError:
    print("Input must be a number")
except ZeroDivisionError:
    print("The average of [] : 0")
