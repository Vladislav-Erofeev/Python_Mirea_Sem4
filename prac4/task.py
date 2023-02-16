import math


def main(n):
    if n == 0:
        return -0.21
    elif n == 1:
        return -0.98
    else:
        return main(n-1) + 1 + math.cos(main(n-2)) ** 2

print(main(7))
