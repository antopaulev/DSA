
def remove_duplicate(arr):
    n  = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        j += 1       
    return i+1

arr = [1,1,2,3,3,4,5,5]
new_length = remove_duplicate(arr)
print("Array after removing duplicates:", arr[:new_length])
print("new length:", new_length)