# Second smallest element
# The problem
# For a list, find the second smallest element in the list

try:
    size = int(input("Enter the size of the array : "))
    user_list = []
    unique_ordered = []
    if size <= 0:
        raise ValueError("Size of array must be a non-zero positive integer")
    if size > 1:
        for _ in range(size):
            user_list.append(float(input("Enter the number : ")))
        unique_ordered = sorted(list(set(user_list)))
        smallest = unique_ordered[0]
        second_smallest = unique_ordered[1]
    else:
        smallest = unique_ordered[0]
        second_smallest = unique_ordered[0]
    print("User list : ", str(user_list))
    print(f"The smallest number : {smallest}")
    print(f"The second smallest number : {second_smallest}")
except ValueError:
    print("List items must be numbers")
