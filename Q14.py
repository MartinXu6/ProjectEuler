n = 1
# while n < 100000000:
#     if n > 4 and (n -1)% 3 == 0 and ((n-1)//3) % 3 != 0 and (n-1)//3 % 2 != 0 :
#         n = (n-1)//3
#     else:
#         n *= 2
#     if n < 1000000:
#         print(n)
x = 818917
chaining = []
for x in range(1, 1000000):
    i = x
    chains = 0
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        chains += 1
    chaining.append([x, chains])
chaining.sort(key=lambda x: x[1])
print(chaining[-1][0])