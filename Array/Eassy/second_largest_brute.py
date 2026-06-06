def second_largest(arr):
    largest = float('-inf')     
    second_largest = float('-inf')
    n = len(arr)
    for i in range (0, n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range (0, n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i] 
    return second_largest

arr = [1, 2, 3, 4, 5]
print("Second largest element in the array is:", second_largest(arr))