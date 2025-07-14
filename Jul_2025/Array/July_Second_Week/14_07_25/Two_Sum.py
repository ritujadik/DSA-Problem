def two_pointer(x,tar):
    left = 0
    right = len(x)-1
    while left < right:
        curr_sum = x[left] + x[right]
        if curr_sum == tar:
            return x[left],x[right]
        elif curr_sum<tar:
            left+=1
        else:
            right-=1
    return None


x = [10,20,35,50]
tar = 25
print(two_pointer(x,tar))
