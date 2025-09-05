def longest_substring_palindrome(x):
    n = len(x)
    max_count = 0
    for i in range(n):
        left = i
        right = i

        while left >= 0 and right < n and x[left] == x[right]:
            max_count = max(max_count,right-left+1)
            left -= 1
            right += 1


        left = i
        right = i+1
        while left >= 0 and right < n and x[left] == x[right]:
            max_count = max(max_count,right-left+1)
            left -= 1
            right += 1
    return max_count


x = "babad"
print(longest_substring_palindrome(x))




