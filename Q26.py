total = 0
for i in range(2,1000):
    num = str(int((1/i)*(10**30)))
    for digit in range(len(num)):
        repeat = 0
        if num.count(num[digit]) > 1:
            repeat = num[digit + 1:].index(num[digit]) + digit + 1
            if num[repeat] != num[-1]:
                if num[digit:digit+8] == num[repeat:repeat + 8]:
                    if repeat - digit == 8:
                        print(repeat - digit,num,1/i,i)
                    total = max(total,repeat -digit)
            break
print(total)