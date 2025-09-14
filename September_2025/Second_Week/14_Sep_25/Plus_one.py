def plus_one(x):
    i = len(x)-1
    while i>=0:
        x[i] +=1
        if x[i]<10:
            return x
        else:
            x[i] = 0
            i-=1

    return [1] + x


x = [9]
print(plus_one(x))

