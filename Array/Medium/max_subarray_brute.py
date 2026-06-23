def find_max_subarray(nums):
    n = len(nums)
    max_sum = float("-inf")
    for i in range(0, n):
        total = 0
        for j in range (i, n):
            total = total + nums[j]
            if total > max_sum:
                max_sum = total
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(find_max_subarray(nums))
