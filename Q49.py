from itertools import permutations

def list_primes(n):
    primes = []
    for i in range(999, n + 1, 2):
        for x in range(2, i // 2 + 1):
            if not i % x:
                break
        else:
            primes.append(i)
    return primes


prime_list = list_primes(10000)
for i in range(len(prime_list)):
    perm = list(map(''.join,(list(permutations(str(prime_list[i]))))))
    for x in perm:
        if int(x) in prime_list[i+1:]:
            if str(int(x) - prime_list[i] + int(x)) in perm and (int(x) - prime_list[i] + int(x)) in prime_list:
                print(prime_list[i],int(x),int(x) - prime_list[i] + int(x))




