"""
Given an input string s and pattern p,implement a regular expression matching with support '.' and '*' where
'.' Matches any single character
'*' Matches zero or more of the preceding element
The matching should cover the entire input string
"""
"""
Ex-1 input:s="aa",p="a"
Output:False
In this "a" does not match the entire string "aa"

Ex-2 input:s="aa",p="a*"
Output:True

Ex-3 input s = "ab",p = ".*"
Output:True

"""
# Approach:1.we have to check whether in pattern we are getting * or . and s == p then it would true else false
#2.take a length of s and length of p too
#3.if string has first char which is in pattern too or will get . then we will proceed further then if that charcter is repating then
# we have to check in pattern we are getting * so that we can repeat preceding char such times and same will proceed for next char upto length
#4.if the above step work then will response true else false

def regular_expression(s,p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(2,n+1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-2]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[m][n]

s = 'ab'
p = '.*'
print(regular_expression(s,p))