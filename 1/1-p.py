"""
1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for반복문을 이용하여 만들어보세요
"""

# 문제 1번


def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i * i
    return s


print(sum(10))

# 문제 2번
# O(1)


# 문제 3번
def sum_1(m):
    return m * (m + 1) * (2 * m + 1) // 6


print(sum_1(10))
