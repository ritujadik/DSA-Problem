# We have to use two pointer approach for the below question
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

def two_sum(nums,tar):
    index_list = list(enumerate(nums))    # step-1 to maintain the original indexes of the given list
    index_list.sort(key=lambda pair : pair[1]) # step-2 we sort the list according to the value of pair which on index 1
    left = 0 #step-3 two pointer approach
    right = len(nums)-1 #step-3 two pointer approach
    while left<=right: # step 4 we are putting the loop
        current_sum = index_list[left][1] + index_list[right][1] # step-5 where we take the value from pair on the left and right basis and add the both in the variable current_sum
        if current_sum == tar: # step-6 here we are comparing both the values current_sum == tar
            return index_list[left][0],index_list[right][0] # step-7  original index of that particular list would be returned
        elif current_sum < tar: # step-8 if current sum is less than target
            left+=1 # step-9 we will move the left by 1
        else:
            right-=1 # step-10 we will move the right by 1


nums = [2,7,11,15]
tar = 9
print(two_sum(nums,tar))