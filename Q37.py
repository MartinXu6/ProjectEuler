def list_primes(n):
    primes = [2]
    for i in range(3,n,2):
        for x in range(3,int(i**0.5) + 1):
            if i % x == 0:
                break
        else:
            primes.append(i)
    return primes
count = 0
prime_list = list_primes(1000000)
truncatable_primes = []
for num in prime_list:
    if num > 10:
        for j in range(1,len(str(num))):
            if int(str(num)[j:]) not in prime_list or int(str(num)[:len(str(num)) - j]) not in prime_list:
                break
        else:
            truncatable_primes.append(num)
print(sum(truncatable_primes))