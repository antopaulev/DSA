# using dictionary
s = "azzyaabcdyaaa"
q =["d","a","b","c","y","z"]


hash_dict = {}
for char in s:
    hash_dict[char] = hash_dict.get(char,0) + 1

for char in q:
    if char in hash_dict:
        print(hash_dict[char])
    else:
        print(0)    