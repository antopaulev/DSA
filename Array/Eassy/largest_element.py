def largest_element(arr):
    largest = arr[0]
    n = len(arr)
    for i in range (0, n):
        if arr[i] > largest:
            largest = arr[i]
    return largest  

arr = [1, 2, 3, 4, 5]
print("Largest element in the array is:", largest_element(arr))

