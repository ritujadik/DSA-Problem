"""
Rotate an array by k position
"""

def rotate_an_array(nums,k):
    k = k % len(nums)
    nums_new = nums[k:] + nums[:k]
    return nums_new


nums = [2,8,9,3,4,7,6]
k = 4
print(rotate_an_array(nums,k))