n =[5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]

hash_dict = {}
for num in n:
    hash_dict[num] = hash_dict.get(num,0) + 1

for num in m:
    if num in hash_dict:
        print(hash_dict[num])

    else:
        print(0)        