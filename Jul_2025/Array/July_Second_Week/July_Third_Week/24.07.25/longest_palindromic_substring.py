#Given a string s, return the longest palindromic substring in s.
#Approach
#1.we will check extreme left end will be equal to extreme right then Left+1 and right+1
# if left is not equal to right then left+=1
# else right -=1
# also mantain max_count which helps to provide the maximum count from all of the 3 condition

def longest_palindrome_substring(x):
    n = len(x)
    max_palindrome = ""
    for i in range(n):
        left,right = i, i
        while left>=0 and right < n and x[left] ==x[right]:
                curr_palindrome = x[left:right+1]
                if len(curr_palindrome) > len(max_palindrome):
                    max_palindrome = curr_palindrome
                left-=1
                right+=1

        left,right = i,i+1
        while left >= 0 and right < n and x[left] == x[right]:
            curr_palindrome = x[left:right+1]
            if len(curr_palindrome) > len(max_palindrome):
                max_palindrome = curr_palindrome
            left-=1
            right+=1
    return max_palindrome


x = "babad"
print(longest_palindrome_substring(x))





