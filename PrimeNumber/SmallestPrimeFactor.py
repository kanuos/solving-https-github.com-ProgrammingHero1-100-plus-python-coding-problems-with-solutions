# Smallest prime factor [premium]
# The problem
# Find the smallest prime factor for the given number.

def is_prime(number):
    number = abs(number)
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def all_factors(number):
    number = abs(number)
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


try:
    n = int(input("Enter a number : "))
    print(f"The factors of {n} are : {all_factors(n)}")
    prime_factors = [x for x in all_factors(n) if is_prime(x)]
    print(f"The prime factors of {n} are : {prime_factors}")
except ValueError:
    print("Input must be a number")
