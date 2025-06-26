#Write a Python function that takes a string and returns the number of vowels (a, e, i, o, u) in it.

def count_vowels(string):
    string = string.lower()
    count = 0
    for vow in string:
        if vow in ["a","e","i","o","u"]:
            count +=1
    return count



string = "Ramesh"
print(count_vowels(string))

