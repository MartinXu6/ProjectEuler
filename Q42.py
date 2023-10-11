words = [i for i in open("words.txt")][0].replace('"',"").split(",")

def triangles(n):
    return [i * (i + 1) // 2 for i in range(1, n + 1)]


triangle_nums = triangles(1000)
total = 0
for word in words:
    if sum([ord(i) - 64 for i in word]) in triangle_nums:
        total += 1
print(total)
