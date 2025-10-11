"""
find the duplicate number in list containing n+1 integers where each integer is between 1 and n
"""

def find_duplicate(nums):
    slow,fast = nums[0],nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow




nums = [3,1,3,4,2]
print(find_duplicate(nums))