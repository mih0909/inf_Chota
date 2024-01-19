def factorize(n: int):
    decomp = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            decomp.append(d)
            n //= d
        d += 1
    if n > 1:
        decomp.append(n)
    return decomp


def count(ls: list):
    st = sorted(list(set(ls)))
    for i in range(len(st)):
        st[i] = ls.count(st[i]) + 1
    return st


def comp(ls: list):
    ls = sorted(ls, reverse=True)
    primes = [2,3,5,7,11,13,17,19,23,27,29]
    product = 1
    for i in range(len(ls)):
        product *= primes[i] ** (ls[i]-1)
    return product


print(comp(factorize(1600)))
print(comp(factorize(1200)))
print(comp(factorize(1000)))
print(comp(factorize(729)))

2095133040
551350800
810810000
901800900


"2095133040 19
551_350_800 17
810_810_000 13
341_510_400 11
