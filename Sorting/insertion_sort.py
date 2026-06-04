nums = [5, 7, 8, 4, 1, 6, 9, 2, 3]
n = len(nums)
def insertion_sort(nums):
    for i in range (1,n):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print(insertion_sort(nums))    