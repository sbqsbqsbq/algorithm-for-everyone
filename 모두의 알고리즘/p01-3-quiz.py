import math


def sum_n_square(n):
    s = 0
    for i in range(0, n + 1):
        s = s + math.pow(i, 2)
    return s


def sum_n_formula(n):
    s = (n * (n + 1) * (2 * n + 1)) // 6
    return s

print(sum_n_formula(10))
