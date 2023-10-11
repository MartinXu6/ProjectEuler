products = []
for multi1 in range(1,10000):
    for multi2 in range(1,10000):
        if "0" not in str(multi1) and "0" not in str(multi2) and "0" not in str(multi1 * multi2):
            if len(str(multi1)) + len(str(multi2)) + len(str(multi1*multi2)) == 9:
                if len(set(str(multi1) + str(multi2) + str(multi1*multi2))) == 9:
                    products.append(multi1*multi2)
print(sum(set(products)))