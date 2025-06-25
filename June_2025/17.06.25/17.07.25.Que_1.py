#Question-Given an array arr[] consisting of only 0's and 1's,
# the task is to find the count of a maximum number of consecutive 1's or 0's present in the array.

def consecutive_one_or_zero(x,target):
    max_count = 0
    count = 0
    for i in x:
        if i == target:
            count += 1
            max_count = max(max_count,count)
        else:
            count = 0
    return max_count



x = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
print(consecutive_one_or_zero(x,target=0))