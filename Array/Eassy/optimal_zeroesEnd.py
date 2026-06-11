def move_zeroes(arr):
    n = len(arr)
    if n == 1:
        return
    i = 0
    while i < n :
        if arr[i] == 0:
            break
        i += 1

    if i == n:
        return  
    j = i + 1
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

arr = [0, 1, 0, 3, 12, 0, 0, 5, 0, 6]
move_zeroes(arr)
print(arr)