# remove duplicate and return non repeted elements



def remove_duplicate(arr):
    n = len(arr)
    unique_elements = {}
    for i in range (0, n):
        unique_elements[arr[i]] = True
    
    j = 0
    for key in unique_elements:
        arr[j] = key
        j += 1

    return j

arr = [1, 2, 3, 2, 4, 5, 1]
new_length = remove_duplicate(arr)
print("Array after removing duplicates:", arr[:new_length])  
print(remove_duplicate(arr))