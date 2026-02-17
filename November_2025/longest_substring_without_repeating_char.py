"""longest substring without repeating char"""

def longest_substring(x):
    new_x = ""
    longest = ""
    for i in x:
        if i not in new_x:
            new_x += i
        else:
            if len(new_x)>len(longest):
                longest = new_x
            index = new_x.index(i)
            new_x = new_x[index+1:] + i

    if (len(new_x)>len(longest)):
        longest = new_x
    return ("new_x:",longest)




x = "pwwkew"
print(longest_substring(x))




