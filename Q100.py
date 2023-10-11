b,n,limit = 3,4,1000_000_000_000
while n <= limit:
    b,n = 3*b+2*n -2, 4*b+3*n -3
print(b,n)