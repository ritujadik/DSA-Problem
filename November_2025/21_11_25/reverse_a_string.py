"""" Reverse a string"""

def reverse_a_word(x):
    x = x.split()
    new_x = x[::-1]
    return " ".join(new_x)


x = "Ritu is the software developer"
print(reverse_a_word(x))

