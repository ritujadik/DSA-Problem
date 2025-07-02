# longest substring without repeating characters

def largest_substirng_without_repetition(x):
    max_length = 0
    start = 0
    seen = {}
    for i in range(len(x)):
        char = x[i]

        if char in seen and seen[char] >= start:
            start = seen[char] + 1

        seen[char] = i
        max_length = max(max_length,i-start + 1)

    return max_length

x = "abcadcabc"
print(largest_substirng_without_repetition(x))