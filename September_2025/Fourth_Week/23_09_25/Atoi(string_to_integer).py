def atoi(x):
    x = x.lstrip()

    if not x:
        return 0

    sign = 1
    i = 0

    if x[i] == '-':
        sign = -1
        i+=1
    elif x[i] == '+':
        i+=1

    num = 0
    while i < len(x) and x[i].isdigit():
        num = num*10+ int(x[i])
        i+=1
    num*=sign

    INT_MAX = 2**31-1
    INT_MIN = -2**31
    if num<-2**31:
        return INT_MIN

    if num>2**31:
        return INT_MAX

    return num


x = "   343  "
print(atoi(x))
