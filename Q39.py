from math import sqrt
from collections import Counter

all_triples = []
for i in range(1001,0,-1):
    for x in range(i -1,0,-1):
        if sqrt(i**2 - x**2).is_integer():
            all_triples.append(sum([i,x,int(sqrt(i**2 - x**2))]))
print(Counter(all_triples))
