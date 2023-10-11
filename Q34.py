def fac(n):
    return 1 if n == 0 else n*fac(n-1)
num = 3
total =0
while True:
    Sum = 0
    for digit in str(num):
        Sum += fac(int(digit))
    if Sum == num:
        total += num
    num += 1
    if num > 100000:
        break
print(total)