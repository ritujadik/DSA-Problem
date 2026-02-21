def two_sum(x,target):
    seen = {}
    for i,num in enumerate(x):
        diff = target - num
        if diff in seen:
            return(seen[diff],i)

        seen[num] = i



x =[2,5,3,7,9,8,1,4]
target = 11
print(two_sum(x,target))
