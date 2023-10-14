from math import isqrt


def numby(num):
    for cur in range(2, isqrt(num) + 1):
        if not num % cur:
            return False
    return True


print(numby(int(input())))
