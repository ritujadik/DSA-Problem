#Sort an array A where each of the elements belong to the set: {0, 1, 2}.
#Expected Time Complexity: O(n)
#Try to solve it without storing the count of 0s, 1s and 2s.

# x = [1,0,1,2,2]
# o_p = [0,1,1,2,2]
def dutch_national_flag(x):
    left =0
    mid = 0
    right = len(x)-1
    while mid<=right:
        if x[mid] == 0:
            x[left],x[mid] = x[mid],x[left]
            left+=1
            mid+=1
        elif x[mid] == 1:
            mid +=1
        else:
            x[mid],x[right] = x[right],x[mid]
            right-=1
    return x

x = [1,0,0,0]
print(dutch_national_flag(x))