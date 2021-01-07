def min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v


v = [5, 6, 90, 82, 1]
print(min(v))
