def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


circular_primes = 1

for num in range(3, 1000001, 2):
    current_num = num
    if is_prime(num):
        for i in range(len(str(num))):
            current_num = str(current_num)[-1] + str(current_num)[:-1]
            if not is_prime(int(current_num)):
                break
        else:
            circular_primes += 1
print(circular_primes)