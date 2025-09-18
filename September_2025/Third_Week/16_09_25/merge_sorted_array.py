def merged_sorted_array(l1,m,l2,n):
    for i in range(n):
        l1.pop()
    l1.extend(l2)
    l1.sort()
    return l1




l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
m = 3
n = 3
print(merged_sorted_array(l1,m,l2,n))


