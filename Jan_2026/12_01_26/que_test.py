def three_sum(x,r):
    x.sort()
    n = len(x)
    result = []
    for i in range(n-2):
        left = 0
        right = n-1

        while left < right:
            total = x[i] + x[left] + x[right]
            if total == r:
                result.append((x[i],x[left],x[right]))
                left+=1
                right-=1
            elif total<r:
                left+=1
            else:
                right-=1
    
        return result


x = [2,1,5,4,3,6]
k = 8
print(three_sum(x,k))
