def reverse(arr,left,right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def right_rotate_k(arr, k):
    n = len(arr)
    k = k % n  
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-k-1)  
    reverse(arr, 0, n-1)  

arr = [1, 2, 3, 4, 5, 6, 7]
k = 4
right_rotate_k(arr, k)
print("Right rotated array:", arr)