
def right_rotate_k(arr, k): 
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    arr[:] = arr[n-k:] + arr[:n-k]  # Rotate the array by slicing


arr = [1, 2, 3, 4, 5, 6, 7]
k = 4
right_rotate_k(arr, k)
print("Right rotated array:", arr)