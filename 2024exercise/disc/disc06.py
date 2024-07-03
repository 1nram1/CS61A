def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add,n


(lambda t : [next(t) for _ in range(10)]) (gen_fib())

next(filter(lambda n : n > 2024,gen_fib()))


def differences(t):
    last_x = next(t)
    for x in t:
        yield x - last_x
        last_x = x


def partitions_gen(n, m):
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        for p in partitions_gen(n - m,m):
            yield p + "+" + str(m)
    if m > 1:
        yield from partitions_gen(n, m - 1)