def fact(a):
    f = 1
    for i in range(1, a+1):
        f = f * i
    return f


print(fact(1))
print(fact(3))
print(fact(10))


def fact_n(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


print(fact_n(1))
print(fact_n(10))
print(fact_n(20))
