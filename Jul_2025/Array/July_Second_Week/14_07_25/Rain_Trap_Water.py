def rain_trap(x):
    if not x:
        return 0
    left = 0
    right = len(x)-1
    max_left = x[left]
    max_right = x[right]
    trapped = 0
    while left<right:
        if x[left]<x[right]:
            left+=1
            max_left = max(max_left,x[left])
            trapped+= max_left - x[left]
        else:
            right-=1
            max_right = max(max_right,x[right])
            trapped+= max_right-x[right]
    return trapped


x = [1,8,6,2,5,4,8,3,7]
print(rain_trap(x))



