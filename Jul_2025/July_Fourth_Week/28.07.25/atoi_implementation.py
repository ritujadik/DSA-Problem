"""
Implement the  myAtoi(string s) function which converts a string to a 32-bit signed integer
The algorithm for myAtoi(string s) is as follows:
1.Whitespace:ignore any leading space(" ")
2.Signedness:Determine the sign by checking if the next character is '-' or '+' assuming postivity if neither present
3.Conversion:Read the integer by skipping leading zeros untill a non-digit character is encountered or the end of the string is reached.
if no digits were read then result is 0
4.Rounding:If the integer is out of 32-bit signed integer range[-2 ** 31 or 2 ** 31 -1],then round the integer to remain in the range
specifically,integers less than -2**31 should be rounded to -2**31 and integers greater than 2**31-1 should be rounded to 2**31-1
Return the integer as a final result
"""

#Approach
#1.first of all we will subtract the digit of the number from 0 ascii value
#2.then will check wether it falls between 0-9 numbers or not
#3.then take a result variable their intiall value would be 0 and we will update conitnuously by multiplying by 10 and added the temp number in that
#4.return result

def myatoi(s):
    n = len(s)
    result = 0
    i = 0
    sign = 1
    while i<n and s[i] == ' ':
        i+=1
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign-=1 if s[i] == '-' else 1
        i+=1
    while i < n and '0'<=s[i] and s[i]<='9':
        digit = ord(s[i]) - ord('0')
        result = result * 10 + digit
        i+=1
    result*=sign

    INTMIN = -2**31
    INTMAX = 2**31-1
    if result<INTMIN:
        return INTMIN
    if result>INTMAX:
        return INTMAX

    return result



s = " 1234 "
print(myatoi(s))