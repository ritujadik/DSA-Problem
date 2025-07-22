def three_sum(x):
    x.sort()
    res = []
    n = len(x)
    for i in range(n-2):
        if i > 0 and x[i] == x[i-1]:
            continue
        left = i+1
        right = n-1

        while left<right:
            current_sum = x[i] +x[left]+ x[right]
            if current_sum==0:
                res.append((x[i],x[left],x[right]))
                left+=1
                right-=1
                while left<right and x[left] == x[left-1]:
                    left+=1
                while left<right and x[right] == x[right+1]:
                    right-=1
            elif current_sum <0:
                left+=1
            else:
                right-=1
    return res


x = [1, 1, 0, -1, -2]
print(three_sum(x))