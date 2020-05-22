"""
선택 정렬
입력:
    리스트 a
출력:
    정렬된 리스트
"""


def select_sort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n - 2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최소값의 위치를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최소값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
select_sort(d)
print(d)