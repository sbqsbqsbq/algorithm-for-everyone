"""
병합 정렬
입력:
    리스트 a
출력:
    없음
"""


def merge_sort(a):
    n = len(a)

    if n <= 1:
        return

    mid = n // 2
    group_1 = a[:mid]
    group_2 = a[mid:]

    merge_sort(group_1)
    merge_sort(group_2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(group_1) and i2 < len(group_2):
        if group_1[i1] < group_2[i2]:
            a[ia] = group_1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = group_2[i2]
            i2 += 1
            ia += 1

    while i1 < len(group_1):
        a[ia] = group_1[i1]
        i1 += 1
        ia += 1

    while i2 < len(group_2):
        a[ia] = group_2[i2]
        i2 += 1
        ia += 1


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)