from itertools import permutations
primes = [2,3,5,7,11,13,17]
result = 0
for perm in list(permutations([str(i) for i in range(10)])):
    if perm[0] != "0":
        for i in range(1,8):
            if int(''.join(perm[i:i+3])) % primes[i-1]:
                break
        else:
            result += int(''.join(perm))
print(result)