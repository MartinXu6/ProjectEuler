
from math import sqrt
def tri(n):
    return int(0.5 * n * (n+1))

x = 1
while True:
    tria = tri(x)
    num = 0
    for i in range(1,tria + 1):
        if i > sqrt(tria):
            num *= 2
            break
        if not tria % i:
            num += 1
    if num > 500:
        break
    x += 1
print(tria)