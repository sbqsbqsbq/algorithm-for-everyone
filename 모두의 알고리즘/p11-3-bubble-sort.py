"""
버블 정렬

입력:
    리스트 a

출력:
    없음
"""


def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n - 2까지
        for j in range(0, n - i - 1):  # 0부터 n - i - 2까지
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)