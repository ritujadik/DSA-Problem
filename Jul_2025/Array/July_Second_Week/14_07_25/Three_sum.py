def three_sum(x,k):
    i = 0
    left = 1
    right = len(x)-1
    while left<right:
        curr_sum = x[left]+x[right]+x[i]
        if curr_sum == k:
            return x[i],x[left],x[right]
        elif curr_sum <k:
            left+=1
        else:
            right-=1

x = [-20,-10,30,35,50]
k = 0
print(three_sum(x,k))
