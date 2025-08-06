"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

def four_sum(nums,target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(0,n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = n-1
            while k<l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k] == nums[k-1]:
                        k+=1
                    while l>k and nums[l] == nums[l+1]:
                        l-=1
                elif total<target:
                    k+=1
                else:
                    l-=1
    return result



nums = [2,2,2,2,2]
target = 8
print(four_sum(nums,target))
