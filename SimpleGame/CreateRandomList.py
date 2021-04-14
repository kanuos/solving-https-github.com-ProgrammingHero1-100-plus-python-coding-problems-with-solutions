import random


def create_random_list(size: int) -> list:
    """
    :param size: returning size of the list
    :return: a random list of integers from 0 to 9
    """
    if size <= 0:
        raise ValueError("Size of list must be a non-zero positive integer")
    result = []
    for _ in range(size):
        result.append(random.randint(0, 9))
    return result
