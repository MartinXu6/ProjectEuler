def fac(n):
    return 1 if n == 1 else fac(n - 1) * n


def combinations(n, r):
    return fac(n) // (fac(r) * fac(n - r))


total = 0
for i in range(1, 101):
    for r in range(1, i):
        if combinations(i, r) > 1000000:
            total += 1
print(total)
