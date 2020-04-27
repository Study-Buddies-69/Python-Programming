def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = i * p
        print(p)


def factorial_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial_recursive(n) * factorial_recursive(n-1)

factorial_recursive(4)