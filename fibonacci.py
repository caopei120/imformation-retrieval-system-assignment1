def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    if n == 2:
        return fib_recur(n - 1)
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(1, 20):
    print(fib_recur(i), end=' ')
