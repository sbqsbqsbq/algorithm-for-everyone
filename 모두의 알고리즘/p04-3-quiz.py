def recursion_sum(n):
    if n == 0:
        return 0
    return n + recursion_sum(n - 1)


def recursion_find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = recursion_find_max(a, n - 1)
    if max_n_1 > a[n - 1]:
        return max_n_1
    else:
        return a[n - 1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(recursion_find_max(v, len(v)))

