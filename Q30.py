num = 2
total = 0
while True:
    total += num if sum([int(i)**5 for i in str(num)]) == num else 0
    num += 1
    if num > 1000000:
        break
print(total)