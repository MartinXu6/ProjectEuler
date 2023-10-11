def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i ==0:
            return False
    return True
max_primes = 0
for b in range(-1000,1001):
    for a in range(-999,1000):
        n = 0
        current_max = 0
        while True:
            if n**2 + a*n +b > 0:
                if is_prime(n**2 + a*n + b):
                    n += 1
                    current_max += 1
                else:
                    if current_max == 71:
                        print(current_max,a,b)
                    max_primes = max(max_primes,current_max)
                    break
            else:
                break
print(max_primes)