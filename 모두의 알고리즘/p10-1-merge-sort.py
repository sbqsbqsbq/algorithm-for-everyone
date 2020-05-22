"""
쉽게 설명한 병합 정렬
입력:
    리스트 a
출력:
    정렬된 리스트
"""


def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눔

    group_1 = merge_sort(a[:mid])  # 재귀 호출로 첫 번째 그룹을 정렬
    group_2 = merge_sort(a[mid:])  # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    result = []
    while group_1 and group_2:  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if group_1[0] < group_2[0]:  # 두 그룹의 맨 앞 자료 값을 비교
            # group_1 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(group_1.pop(0))
        else:
            # group_2 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(group_2.pop(0))

    # 아직 남아있는 자료들을 결과에 추가
    # group_1과 group_2 중 이미 빈 것은 while을 바로 지나감

    while group_1:
        result.append(group_1.pop(0))

    while group_2:
        result.append(group_2.pop(0))

    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))