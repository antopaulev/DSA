def find_max_subarray(nums):
    n = len(nums)
    max = float("-inf")
    total = 0
    for i in range(0, n):
        total = total + nums[i]
        if total > max:
            max = total
        if total < 0:
            total = 0
    return max
            

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(find_max_subarray(nums))