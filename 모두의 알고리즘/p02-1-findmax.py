def find_max(a):
    n = len(a)  # 입력 크기 n
    max_index = 0
    max_v = a[0]  # 리스트의 첫 번째 값을 최대값으로 기억
    for i in range(1, n):  # 1부터 n-1까지 반복
        if a[i] > max_v:  # 이번 값이 현재까지 기억된 최대값보다 크면
            max_index = i
            max_v = a[i]  # 최대값을 변경
    return max_v, max_index


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v)[1])