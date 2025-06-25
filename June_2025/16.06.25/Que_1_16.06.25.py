# we need to find the distinct second largest number if there is no second largest number then return -1

def second_largest_number(x):
    x1 = set(x)
    if len(x1) == 0 or len(x1) == 1:
        return -1
    else:
        y = sorted(x1)
        return(y[-2])

x = [9,4,5,7,8,2,11,11]
print(second_largest_number(x))



