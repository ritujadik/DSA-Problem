#Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target. This problem is a variation of 2Sum problem.

def pair_of_sum(arr,target):
    new_set = set()
    pairs = []
    for i in arr:
        complement = target-i
        if complement in new_set:
            pairs.append((complement,i))
        new_set.add(i)
    return pairs

arr = [2,3,5,7,9,1,6]
target = 8
print(pair_of_sum(arr,target))
