ways = 0

for two in range(2):
    for one in range(3):
        for fifty in range(5):
            for twenty in range(11):
                for ten in range(21):
                    for five in range(41):
                        for tw in range(101):
                            if (two*200 + one*100 + fifty*50 + twenty*20 + ten*10 + five*5 + tw*2) <= 200:
                                print(two,one,fifty,twenty,ten,five)
                                ways += 1
print(ways)