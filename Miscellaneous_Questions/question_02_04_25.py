x = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(x) - 1:
    if x[i] > x[i+1]:
        x.pop(i+1)
    else:
        x.pop(i)
print(x)

