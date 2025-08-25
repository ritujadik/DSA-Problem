"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

def three_sum_close(nums,tar):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n-2):
        left = i+1
        right = n-1
        while left<right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum-tar) < abs(closest_sum-tar):
                closest_sum = current_sum
            if current_sum<tar:
                left+=1
            elif current_sum>tar:
                right-=1
            else:
                return tar
    return closest_sum


nums = [0,0,0]
tar = 1
print(three_sum_close(nums,tar))



