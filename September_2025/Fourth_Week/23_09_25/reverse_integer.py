def reverse_integer(x):
    result = 0
    x = int(x)
    sign = 1 if x>0 else -1
    x = abs(x)
    while x!=0:
        temp = x%10
        result = result*10 + temp
        x = x//10
    result = result*sign
    if result<-2**31 or result>2**31-1:
        return 0
    return result


x = 123
print(reverse_integer(x))
