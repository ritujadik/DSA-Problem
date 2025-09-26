def four_sum(x,k):
    x.sort()
    n = len(x)
    x_new = []
    for i in range(n):
        if i>0 and x[i] == x[i-1]:
            continue

        for j in range(i+1,n):
            if j > 0 and x[j] == x[j-1]:
                continue

            left = j+1
            right = n-1
            while left<right:
                current_sum = x[left] + x[right] + x[j] + x[i]
                if current_sum==k:
                    x_new.append([x[i],x[j],x[left],x[right]])
                    left+=1
                    right-=1

                    while left<right and x[left] == x[left-1]:
                        left+=1

                    while left<right and x[right] == x[right+1]:
                        right-=1

                elif current_sum<k:
                    left+=1

                else:right-=1
    return x_new


x = [1,0,-1,0,-2,2]
k = 0
print(four_sum(x,k))



