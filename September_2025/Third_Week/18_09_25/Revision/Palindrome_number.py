def palindrome_number(x):
    orignal_num = x
    new_num = 0
    while x > 0:
        y = x % 10
        new_num = new_num*10 + y
        x = x//10

    if new_num == orignal_num:
        return ("this is a palindrome number")

    else:
        return ("this is not a palindrome number")





x = 123
print(palindrome_number(x))
