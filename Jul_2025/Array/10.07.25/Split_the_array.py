#You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
#nums1.length == nums2.length == nums.length / 2.
#nums1 should contain distinct elements.
#nums2 should also contain distinct elements.
#Return true if it is possible to split the array, and false otherwise.

"""Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4]."""

def splitsubarray(nums):
    new_len = len(nums)
    num1 = []
    num2 = []
    new_length = new_len//2

    # while len(num1) < new_length:
    for i in range(len(nums)):
        if nums[i] not in num1 and len(num1) < new_length:
            num1.append(nums[i])
        else:
            num2.append(nums[i])

    if len(num1) == len(num2) == new_length and len(set(num1)) == new_length and len(set(num2)) == new_length:
        return True
    else: return False



nums = [1,1,1,1]
print(splitsubarray(nums))