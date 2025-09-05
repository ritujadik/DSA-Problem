def reverse_list(x):

    left = 0
    right = len(x)-1

    while left<right:
        x[left],x[right] = x[right],x[left]
        left+=1
        right-=1
    return(x)



x = [3,4,2,5,6,7]
print(reverse_list(x))