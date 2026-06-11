def max_consecutive(arr):
    max_count = 0
    count = 0
    n = len(arr)
    for i in range(0,n):
        if arr[i] == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
                count = 0

    if max_count > count:
        return max_count
    else:
        return count

arr = [1, 1, 0, 1, 1, 1, 0, 1,1,1,1]
print(max_consecutive(arr))