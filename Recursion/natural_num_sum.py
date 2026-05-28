# sum of first n natural numbers using recursion

def func(n):
    if n <= 1:
        return n
    return n + func(n - 1)

print(func(5))