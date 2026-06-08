def right_rotate(arr):
    n = len(arr)
    last_element = arr[n-1]
    for i in range (n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = last_element

arr = [1, 2, 3, 4, 5]
right_rotate(arr)
print("Right rotated array:", arr)