# Que-Python program to check whether the string is Symmetrical or Palindrome

def string_is_palindrome(x):
        if x == x[::-1]:
            print("This is palindrome:",x)
        else:
            print("this is not a palindrome",x)

def string_is_symmetrical(x):
    mid = len(x)//2
    if len(x)%2 == 0:
        first_half = x[:mid]
        second_half = x[mid:]
        if first_half == second_half:
            print("this is a symmetrical string",x)
        else:
            print("it is not a symetrical",x)
    else:
        print("this is not a symmterical")

    string_is_palindrome(x)

x = "amama"
string_is_symmetrical(x)

