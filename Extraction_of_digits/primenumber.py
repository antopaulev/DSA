n = 77
num = n
count = 0
for i in range(1,n+1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("not a prime")