"""
1. array에서 첫번째 숫자를 기억
2. 두번째 숫자와 비교하여 더 큰것을 기억
3. array의 끝까지 반복.
4. 마지막으로 기억된 숫자가 최댓값
"""


def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v


v = [12, 45, 67, 89, 91, 1, 4]
print(find_max(v))
