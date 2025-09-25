def three_sum(x,k):
    x.sort()
    n = len(x)
    result = []

    for i in range(n-2):
        if i>0 and x[i] == x[i-1]:
            continue

        left = i+1
        right = n-1
        while left<right:
            current_sum = x[left] + x[right] + x[i]
            if current_sum == k:
                result.append((x[left],x[right],x[i]))

                while left<right and x[left] == x[left+1]:
                    left+=1

                while left<right and x[right] == x[right-1]:
                    right-=1

                left+=1
                right-=1

            elif current_sum<k:
                left+=1

            else:right-=1

    return result


x = [-1,0,1,2,-1,-4]
k = 0
print(three_sum(x,k))


