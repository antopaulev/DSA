def find_missing_number(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

arr = [0, 1, 2, 3, 4, 5, 6, 7, 9]
print(find_missing_number(arr))