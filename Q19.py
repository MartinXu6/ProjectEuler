day = 2
total = 0
leap_year = False
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for year in range(1901,2001):
    if year % 100 == 0:
        leap_year = True if year % 400 == 0 else False
    else:
        leap_year = True if year % 4 == 0  else False
    months[2] = 29 if leap_year else 28
    for month in range(1,13):
        if day == 0:
            total += 1
        day = (day + months[month])%7
print(total)