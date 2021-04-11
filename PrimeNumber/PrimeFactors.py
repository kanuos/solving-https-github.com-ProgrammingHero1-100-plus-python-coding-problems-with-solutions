# Calculate Prime Factors
# A number has both prime and non-prime factors. Isolate the primes

def is_prime(number):
    number = abs(number)
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def calculate_prime_factors(number):
    __factors = []
    for i in range(1, number):
        if number % i == 0 and is_prime(i):
            __factors.append(i)
    return __factors


print(calculate_prime_factors(15))
print(calculate_prime_factors(25))
print(calculate_prime_factors(140))
print(calculate_prime_factors(31))
