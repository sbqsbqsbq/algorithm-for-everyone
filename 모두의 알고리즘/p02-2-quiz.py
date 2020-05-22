def find_min(a):
    n = len(a)
    v_max = 0

    for i in range(0, n):
        if a[i] > v_max:
            v_max = a[i]

    for i in range(0, n):
        if a[i] < v_max:
            v_max = a[i]

    return v_max


a = [10, 2, 3, 4, 5, 9, 92, 78, 100]
print(find_min(a))