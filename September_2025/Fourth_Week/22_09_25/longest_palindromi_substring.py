def longest_palindromic_substring(s):
    def expand_center(left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]

    max_palindrome = ""
    for i in range(len(s)):
        odd = expand_center(i,i)
        even = expand_center(i,i+1)

        max_palindrome = max(max_palindrome,odd,even,key=len)

    return max_palindrome





s = "babad"
print(longest_palindromic_substring(s))