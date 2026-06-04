# accending order
nums = [5,7,8,4,1,6,9,2,3]
n = len(nums)
def selection_sort(nums):
    for i in range (0,n):
        min_idx = i
        for j in range (i+1,n):
            if nums[j]< nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums

print(selection_sort(nums)) 
