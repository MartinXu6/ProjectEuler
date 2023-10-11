def list_prime(n):
    primes = [2]
    for i in range(3, n, 2):
        for x in range(3, int(i ** 0.5) + 1):
            if i % x == 0:
                break
        else:
            primes.append(i)
    return primes


prime_list = list_prime(10000)
consecutive = 0
ans = []
for num in range(10000):
    divisible_prime = 0
    current_number = num
    for prime in prime_list:
        if prime >= current_number:
            consecutive = 0
            break
        if current_number % prime == 0:
            if num == 13403:
                print(prime)
            divisible_prime += 1
            while current_number % prime == 0:
                current_number //= prime
        if divisible_prime == 3 and current_number == 1:
            consecutive += 1
            break
        elif divisible_prime > 3:
            consecutive = 0
            break
        elif divisible_prime < 3 and current_number == 1:
            consecutive = 0
            break
    if consecutive == 3:
        ans.append([num, num -1,num - 2])
        consecutive = 0
print(ans)

