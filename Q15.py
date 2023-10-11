routes = 0


def fac(n):
    return 1 if n == 0 else n * fac(n - 1)


def choices(how_many, num):
    total = 1
    for i in range(num):
        total *= how_many
        how_many -= 1
    total //= fac(num)
    return total


print(choices(40,20))