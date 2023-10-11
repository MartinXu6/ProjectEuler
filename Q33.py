numerator = []
denominator = []
for a in range(10,100):
    for b in range(10,100):
        if a % 10 and b % 10 and a!= b and a < b:
            for digit in range(10):
                if str(digit) in str(a) and str(digit) in str(b):
                    index1, index2 = 1 - str(a).index(str(digit)), 1 - str(b).index(str(digit))
                    if int(str(a)[index1])/int(str(b)[index2]) == a/b:
                        numerator.append(a)
                        denominator.append(b)
print(numerator)
print(denominator)