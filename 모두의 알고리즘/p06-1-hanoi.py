"""
하노이의 탑
    입력:
        옮기려는 원반의 개수 n
        원반을 옮길 도착점 기둥 to_pos
        옮기는 과정에서 사용할 보조 기둥 aux_pos
    출력:
        원반을 옮기는 순서
"""


def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:  # 원반을 한 개 옮기는 문제면 그냥 옮기면 됨.
        print(from_pos, " -> ", to_pos)
        return

    # 원반 n - 1개를 aux_pos로 이동 (to_pos를 보조 기둥으로)
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, " -> ", to_pos)
    # aux_pos에 있는 원반 n - 1개를 목적지로 이동 (from_pos를 보조 기둥으로)
    hanoi(n - 1, aux_pos, to_pos, from_pos)


print("n = 20")
hanoi(20, 1, 3, 2)