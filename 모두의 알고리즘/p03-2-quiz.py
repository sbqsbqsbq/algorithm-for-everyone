def make_mate(a):
    n = len(a)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(a[i] + " - " + a[j])

make_mate(["Tom", "Jerry", "Mike", "Micheal", "Jane"])