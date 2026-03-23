"""
Given an array consisting of only 0s and 1s.find the longest contiguous sequence of either 1s or 0s in the array
"""

def continuous_one(arr):
    max_count,count = 0,1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            max_count = max(max_count,count)
            count = 1

    return max(max_count,count)


arr = [1,0,0,1,1,0,1,1,1,1]
print(continuous_one(arr))


