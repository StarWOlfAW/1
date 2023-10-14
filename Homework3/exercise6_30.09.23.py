from math import sqrt, ceil


def numby(num=int, cur=2, c=0):
    c = ceil(sqrt(num))
    for cur in range(2, c):
        if num % cur == 0:
            return False
            break
        return True


print(numby(int(input())))
