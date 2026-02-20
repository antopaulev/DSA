n = 153
num = n
pow = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + (digit ** pow)
    num = num // 10

print(n == total)