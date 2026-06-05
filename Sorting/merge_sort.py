
arr = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    result =  merge(left_half, right_half)
    return result

def merge(left, right):
    merged = []
    i, j = 0, 0
    n , m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < n:
        merged.append(left[i])
        i += 1
    while j < m:
        merged.append(right[j])
        j += 1
    return merged

print(merge_sort(arr))