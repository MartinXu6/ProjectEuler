def pentagon(n):
    return [i * (3 * i - 1) // 2 for i in range(1, n + 1)]


def is_pentagon(x):
    current = 1
    while True:
        if current * (3 * current - 1) // 2 == x:
            return True
        if current * (3 * current - 1) // 2 > x:
            return False
        current += 1


pentagons = pentagon(10000)
for first in range(len(pentagons)):
    for second in range(len(pentagons[first:])):
        print(pentagons[second])
        if is_pentagon(pentagons[first] + pentagons[second]):
            if is_pentagon(pentagons[second] - pentagons[first]):
                print(pentagons[first], pentagons[second])
