from math import sqrt

def list_primes(n):
    prime_list = [2]
    for i in range(3,n+1,2):
        for x in range(3,int(sqrt(i))+1):
            if i % x == 0 :
                break
        else:
            prime_list.append(i)
    return prime_list
primes = list_primes(10000)
composite = [i for i in range(9,10000,2) if i not in primes]
for i in composite:
    for prime in primes:
        if prime < i:
            if sqrt((i - prime)//2).is_integer():
                break
        else:
            print(i)
            exit()