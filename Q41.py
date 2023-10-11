from itertools import permutations

perms = sorted([int("".join(i)) for i in list(permutations(["1", "2", "3", "4", "5", "6", "7"])) if not i[6] == "6" and not i[6] == "4" and not i[6] == "2" and not i[6] == "5"], reverse=True)


def is_prime(n):
    for i in range(3, n // 2):
        if n % i == 0:
            return False
    else:
        return True
for x in perms:
    if is_prime(x):
        print(x)
        break