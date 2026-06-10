def right_rotate_by_k(arr, k):  
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    while k > 0:
        last_element = arr[n-1]
        for i in range (n-2, -1, -1):
            arr[i+1] = arr[i]
        arr[0] = last_element
        k -= 1

arr = [1, 2, 3, 4, 5]
k = 3
right_rotate_by_k(arr, k)
print(arr)