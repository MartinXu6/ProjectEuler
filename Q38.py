largest = 0
for num in range(1, 9999):
    concatenated = ""
    for n in range(1, 10):
        if len(set(concatenated)) == 9 and len(concatenated) == 9:
            largest = max(largest, int(concatenated))
            break
        elif len(concatenated) > 9:
            break
        else:
            concatenated += str(n * num)
            if "0" in concatenated:
                break
print(largest)