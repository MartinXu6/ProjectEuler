def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(sum(list(map(int, list(str(fac(100)))))))
