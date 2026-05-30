nums = [1,2,3,4,4,5,6,5,4,7,8,9,2,9,9,9,]
n = len(nums)

frq_dict = {}
for i in range (0,n):
    frq_dict[nums[i]] = frq_dict.get(nums[i],0) + 1

print(frq_dict) 
 