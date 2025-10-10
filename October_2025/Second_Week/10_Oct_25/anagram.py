"""
two strings are anagram

"""

def anagram(x1,x2):
    n1 = len(x1)
    n2 = len(x2)
    if n1 != n2:
        return False

    return sorted(x1) == sorted(x2)



x1 = "listen"
x2 = "silent"

print(anagram(x1,x2))
