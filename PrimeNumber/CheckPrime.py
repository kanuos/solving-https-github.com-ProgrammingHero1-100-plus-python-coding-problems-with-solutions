# Check prime
# Enter a number and check whether the number is prime or not

def is_prime(number: int):
    if number == 0 or number == 1:
        return False
    number = abs(number)
    factor = 0
    for i in range(2, number):
        if number % i == 0:
            factor += 1
    return factor == 0


print(is_prime(13))
print(is_prime(31))
print(is_prime(55))
print(is_prime(53))
