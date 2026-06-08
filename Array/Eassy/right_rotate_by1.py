# right rotate an array by 1

def right_rotate(arr):
    n = len(arr)
    arr [:] = [arr[n-1]] + arr[0:n-1]

arr = [1, 2, 3, 4, 5]
right_rotate(arr)
print("Right rotated array:", arr)