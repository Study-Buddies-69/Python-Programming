from functools import lru_cache


@lru_cache()
def fibonacci_for_the_number_n(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci_for_the_number_n(n-1) + fibonacci_for_the_number_n(n-2)


def fibonacci_for_the_first_n_numbers(n):
    for i in range(1, n+1):
        print("Fibonacci number {} is {}".format(i, fibonacci_for_the_number_n(i)))


fibonacci_for_the_first_n_numbers(100)
