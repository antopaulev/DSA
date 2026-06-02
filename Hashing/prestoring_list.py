# prestoring values in a list for faster access
# this is a common technique used in hashing to avoid collisions and improve performance
#constraints:
# i<=n[i]<=10
# n can have 10^8 elements
# m can have 10^8 elements

n =[5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]
hash_list = [0]*11

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])
