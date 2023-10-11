from math import sqrt


def list_factors(n):
    factors = [n // x + x for x in range(2, int(n ** 0.5) + 1) if n % x == 0]
    if sqrt(n).is_integer():
        return sum(factors) + 1 - int(sqrt(n))
    return sum(factors) + 1


abundant = [i for i in range(1, 28124) if list_factors(i) > i]
bad_list = []
for x in range(1,28124):
    print(x)
    for item in abundant:
        if item < x:
            if x - item in abundant:
                break
    else:
        bad_list.append(x)
print(sum(bad_list))