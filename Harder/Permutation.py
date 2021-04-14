# The Problem
# Find all permutation of a given list.
import itertools

try:
    user_list = list(input("Enter the numbers separated by space : ").split(' '))
    print(user_list)
    sample = itertools.permutations(user_list)
    print(list(sample))
except ValueError as err:
    print(err)
