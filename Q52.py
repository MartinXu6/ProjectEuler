from collections import Counter
for i in range(1,1000000):
    if Counter(str(i)) == Counter(str(2*i)) == Counter(str(3*i)) == Counter(str(4*i)) == Counter(str(5*i)) == Counter(str(6*i)):
        print(i)
        break