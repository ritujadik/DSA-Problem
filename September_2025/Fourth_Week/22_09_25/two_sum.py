def two_sum(x,k):
    x_new = list(enumerate(x))
    x_new.sort(key=lambda pairs:pairs[1])
    left = 0
    right = len(x)-1
    while left<right:
        current_sum = x_new[left][1] + x_new[right][1]
        if current_sum == k:
            return(x_new[left][0],x_new[right][0])

        elif current_sum<k:
            left+=1

        else:
            right-=1

    return None


x = [2,7,11,15]
k = 9

print(two_sum(x,k))

