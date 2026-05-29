# Reverse array using recursion
def reverse_array(nums, left, right):
    if left>= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverse_array(nums, left + 1, right - 1)                
# test the function
arr = [1, 2, 3, 4, 5]   
reverse_array(arr, 0, len(arr) - 1)
print(arr)  # Output: [5, 4, 3, 2, 1]