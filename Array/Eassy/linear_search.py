def linear_search(arr,target):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == target:
            return i
    return -1
arr = [1, 2, 3, 4, 5]
target = 100 
print(linear_search(arr, target))   