# Second Largest
# The problem
# For a list, find the second largest number in the list.

try:
    size = int(input("Enter the size of the array : "))
    user_list = []
    if size <= 0:
        raise ValueError("Size of array must be a non-zero positive integer")
    for _ in range(size):
        user_list.append(float(input("Enter the number : ")))
    largest = max(user_list)
    second_largest = min(user_list)
    for num in user_list:
        if largest > num > second_largest:
            second_largest = num
        if num == largest:
            continue
    print("User list : ", str(user_list))
    print(f"The largest number : {largest}")
    print(f"The second largest number : {second_largest}")
except ValueError:
    print("List items must be numbers")
