#Given a string s, find the length of the longest substring without duplicate characters.
def longest_substring_without_repeating_char(x):
    n = len(x)
    max_count = 0
    seen = set()
    start = 0

    for i in range(n):
        while x[i] in seen:
            seen.remove(x[start])
            start+=1
        seen.add(x[i])
        curr_count = i - start + 1

        max_count = max(max_count,curr_count)

    return max_count


x = "abcabcabc"
print(longest_substring_without_repeating_char(x))






