total = 0
names = sorted(list(open("0022_names.txt"))[0].split(","))
for name in range(len(names)):
    Sum = 0
    for letter in names[name]:
        if letter != '"':
            Sum += ord(letter) -64

    Sum *= name + 1
    total += Sum
print(total)