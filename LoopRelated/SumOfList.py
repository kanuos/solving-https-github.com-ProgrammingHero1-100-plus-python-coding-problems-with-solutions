# For a given list, get the sum of each number in the list

import random

try:
    size = int(input("Enter the size of the list : "))
    if size <= 0:
        raise ValueError("Size of array must be a non-zero positive integer")
    random_list = []
    for _ in range(size):
        num = random.randint(0, 10000)
        random_list.append(num)
    print(f"The computer generated list : {random_list}")
    print(f"The sum of the entered array : {sum(random_list)}")
except ValueError:
    print("The size of array must be an integer")
