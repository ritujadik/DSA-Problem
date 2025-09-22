def longest_substring_without_repetiton(x):
    x_new = ""
    max_count = 0
    for i in x:
        if i not in x_new:
            x_new += i
        else:
            x_new = x_new[x_new.index(i) + 1:] + i

        max_count = max(max_count,len(x_new))

    return max_count



x = "abcabcabc"
print(longest_substring_without_repetiton(x))