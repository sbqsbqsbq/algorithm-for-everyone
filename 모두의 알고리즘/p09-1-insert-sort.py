"""
쉽게 설명한 삽입 정렬
입력:
    리스트 a
출력:
    정렬된 리스트
"""


# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_insert_index(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0, len(r)):
        # v 값보다 i번 위치에 있는 자료 값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < r[i]:
            return i

    # 적절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(r)


def insert_sort(a):
    result = []  # 새 리스트를 만들어 정렬된 값을 저장
    while a:  # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0)
        insert_index = find_insert_index(result, value)
        result.insert(insert_index, value)
    return result


d = [2, 4, 5, 1, 3]
print(insert_sort(d))
