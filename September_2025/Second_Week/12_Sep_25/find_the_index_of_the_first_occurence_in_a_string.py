def index_of_first_string(haystack,needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1




haystack = "sadbutsad"
needle = "sad"
print(index_of_first_string(haystack, needle))