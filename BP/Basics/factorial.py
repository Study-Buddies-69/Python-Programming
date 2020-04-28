def factorial_basic(n):
    p = 1
    for i in range(1, n + 1):
        p = i * p
        print(p)


def factorial_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(5))
