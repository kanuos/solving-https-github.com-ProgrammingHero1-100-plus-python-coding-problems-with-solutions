# Largest element of a list
# The problem
# Find the largest element of a list.

try:
    size = int(input("Enter the size of the array : "))
    user_list = []
    if size <= 0:
        raise ValueError("Size of array must be a non-zero positive integer")
    for _ in range(size):
        user_list.append(float(input("Enter the number : ")))
    largest = user_list[0]
    for num in user_list:
        if num > largest:
            largest = num
    print("User list : ", str(user_list))
    print(f"The largest number : {largest}")
except ValueError:
    print("List items must be numbers")
