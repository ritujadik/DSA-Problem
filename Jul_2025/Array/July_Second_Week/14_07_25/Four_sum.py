def four_sum(x,k):
    i = 0
    j = 1
    left = 2
    right = len(x)-1
    while left<right:
        curr_sum = x[i] + x[j] + x[left] + x[right]
        if curr_sum == k:
            return x[i],x[j],x[left],x[right]
        elif curr_sum<k:
            left+=1
        else:
            right-=1
    return None

x = [5,5,5,5,30,40,50,55,60]
k = 20
print(four_sum(x,k))