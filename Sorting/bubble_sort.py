nums = [5, 7, 8, 4, 1, 6, 9, 2, 3]
n = len(nums)
def bubble_sort(nums):
    for i in range (n-2,-1,-1):
        is_swapped = False
        for j in range (0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swapped = True
        if not is_swapped:
            break
    return nums

print(bubble_sort(nums))    