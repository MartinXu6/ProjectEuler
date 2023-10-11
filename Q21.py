factor_sum = []
total = 0


def list_factors(n):
    factors = [n // x + x for x in range(2, int(n ** 0.5) + 1) if n % x == 0]
    return sum(factors) + 1


for i in range(10001):
    factor_sum.append(list_factors(i))
for x in range(10001):
    if factor_sum[x] <= 10000:
        if factor_sum[factor_sum[x]] == x and factor_sum[x] != x:
            total += x + factor_sum[x]
print(total//2)