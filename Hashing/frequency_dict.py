# store frequency of each character in a dictionary
nums =[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
frq_dict = dict()
for i in range (0,len(nums)):
    if nums[i] in frq_dict:
        frq_dict[nums[i]] += 1
    else:
        frq_dict[nums[i]] = 1

print(frq_dict)         
