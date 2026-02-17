"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
nums = [2,7,11,15]
target = 9
"""

def two_sum(nums,target):
    left = 0
    right = len(nums)-1
    while left<right:
        total = nums[left] + nums[right]
        if total == target:
            return left,right
        elif total < target:
            left+=1
        else:
            right-=1

    return None

nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))


