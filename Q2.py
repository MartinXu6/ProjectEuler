Fibo = [1,2]
index = 2
while True:
    sUm = Fibo[index - 1 ]+ Fibo[index - 2]
    if sUm <= 4000000:
        Fibo.append(sUm)
    else:
        break
    index += 1
print(sum(i for i in Fibo if not i % 2 ))
