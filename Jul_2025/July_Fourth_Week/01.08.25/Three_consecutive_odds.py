"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""
def odd_num(x):
    count = 0
    for i in x:
        if i%2 !=0:
            count+=1
            if count == 3:
                return True
        else:
            count=0
    return False



x = [2,6,4,1]
print(odd_num(x))