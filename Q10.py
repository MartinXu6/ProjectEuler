def primes(n):
    prime_list = [2,]
    for i in range(3, n,2):
        for j in range(3,i//3):
            if not i % j:
                break
        else:
            prime_list.append(i)
    return prime_list


print(sum(primes(2000000)))
