"""
리스트에 숫자가 n개 있다면 가장 큰 값이 있는 위치번호를 돌려주는 알고리즘을 만드십시오.
"""


def max_pos(a):
    n = len(a)
    max_v = 0
    for i in range(1, n):
        if a[i] > a[max_v]:
            max_v = i
    return max_v


v = [1, 2, 91, 67, 9]
print(max_pos(v))
