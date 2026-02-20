from math import sqrt
n = 36
num = n
res = []

for i in range (1,int(sqrt(num))+1):
    if num % i == 0:
        res.append(i)
        if num // i != i:
            res.append(num // i)

res.sort()
print(res)
