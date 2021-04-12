# Armstrong number.
# A number is an Armstrong Number or narcissistic number
# if it is equal to the sum of its own digits raised to the power of the number of digits.

def is_armstrong(number: int) -> bool:
    sum_of_cubes = 0
    temp = number
    while temp > 0:
        sum_of_cubes += (temp % 10) ** 3
        temp //= 10
    return sum_of_cubes == number


def nearest_armstrong(number):
    pre = 0
    print("Checking for nearest Armstrong Numbers. Please wait...")
    for i in range(number, 1, -1):
        if is_armstrong(i):
            pre = i
            break
    while True:
        number += 1
        if is_armstrong(number):
            post = number
            break
    print("Found nearest Armstrong Numbers")
    return pre, post


try:
    num = int(input("Enter a number : "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an Armstrong Number")
        before, after = nearest_armstrong(num)
        print(f"The nearest Armstrong Numbers of {num} are {before} and {after}")
except ValueError:
    print("Input must be a number")
