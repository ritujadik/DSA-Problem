def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)



x = factorial(67)
print(x)