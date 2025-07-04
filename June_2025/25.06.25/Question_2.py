# Two sum
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""

def two_sum(num,target):
    n = len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i] + num[j] == target:
                return [num[i],num[j]]

    return ("no elment who has the sum equal to target")


num = [3,2,4]
target = 6
print(two_sum(num,target))