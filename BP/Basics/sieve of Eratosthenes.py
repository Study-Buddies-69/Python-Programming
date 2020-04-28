def primes_under_n(n):
    primes_array = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes_array[p]:
            for x in range(p*2, n+1, p):
                primes_array[x] = False
        p += 1

    primes_array[0] = False
    primes_array[1] = False

    for x in range(n + 1):
        if primes_array[x]:
            print(x)


primes_under_n(20)