"""
1부터 n까지합의 알고리즘을 재귀호출로 작성하라

"""

# 1. 1부터 n까지의 합을 구하는 알고리즘


def sum_(n):
    if n < 1:
        return 0
    return n + sum_(n-1)


print(sum_(1))
print(sum_(5))
print(sum_(10))

# 2. 숫자 중 최댓값을 구하는 알고리즘을 재귀 호출로 작성하십시오.


def max_n
