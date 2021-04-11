# All Prime Numbers
# the problem
# Ask the user to enter a number. Then find all the primes up to that number.

try:
    n, p = int(input("Enter a number : ")), 2
    all_primes = [False, False]
    all_primes.extend([True] * (n - 1))
    while p ** 2 <= n:
        if all_primes[p]:
            for i in range(p * 2, n + 1, p):
                all_primes[i] = False
        p += 1
    all_primes = [i for i in range(len(all_primes)) if all_primes[i]]
    print(all_primes)
except ValueError:
    print("Input must be a number")
