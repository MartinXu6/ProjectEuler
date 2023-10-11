fibo_list = [1,1,2]
print(fibo_list)
index = 3
while True:
    num = fibo_list[index-1] + fibo_list[index - 2]
    if num < 10**999:
        fibo_list.append(fibo_list[index-1] + fibo_list[index - 2])
    else:
        print(index)
        break
    index += 1