x = [2,4,6,5,9]
x_new  = 7
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] + x[j] == x_new:
            print((x[i],x[j]))