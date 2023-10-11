num = 10405071317

print(sum([int(str(i**i)[-10:]) for i in range(11,1000) if i % 10]) + num)