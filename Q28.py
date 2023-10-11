# dia1 = 0

# dia2 = 0
# dia3 = 0
# dia4 = 0
total = 0
for i in range(1,1002,2):
    # dia1 = i**2
    # dia2 = i**2-(3*(i-1))
    # dia3 = i**2 - (2*(i-1))
    # dia4 = i**2 -(i-1)
    total += 4*(i**2) - 6*(i-1)
# print(sum([dia1,dia2,dia3,dia4]) - 3)
print(total -3)