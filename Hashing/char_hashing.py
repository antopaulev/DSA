
s = "azzyaabcdyaaa"
q =["d","a","b","c","y","z"]

hash_list = [0]*26
for char in s:
    ascii_value = ord(char)
    index = ascii_value - 97
    hash_list[index] += 1

for char in q:
    ascii_value = ord(char)
    index = ascii_value - 97
    print(hash_list[index])

