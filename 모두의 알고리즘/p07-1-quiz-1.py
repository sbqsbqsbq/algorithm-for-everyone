"""
찾는 값이 리스트고,
리턴하는 값도 리스트일 때
"""


def search_list(a, x):
    """

    :param a: 들어가는 리스트
    :param x: 찾고자 하는 값 리스트
    :return:
    """

    n = len(a)
    return_list = []

    for i in range(0, n):
        for j in range(0, len(x)):
            if a[i] == x[j]:
                return_list.append(i)

    return return_list


v = [17, 92, 18, 33, 58, 7, 42]
print(search_list(v, [18, 33, 7]))
print(search_list(v, [33]))
print(search_list(v, [900]))
