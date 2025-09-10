def divide(dividend,divisor):
    INT_MAX = 2**31-1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend<0) !=(divisor<0)

    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0

    while dividend>=divisor:
        temp = divisor
        multiple = 1
        while dividend>=temp+temp:
            temp += temp
            multiple+=multiple

        dividend-=temp
        quotient+=multiple

    if negative:
        quotient = -quotient

    return max(min(quotient,INT_MAX),INT_MIN)



print(divide(7,3))
