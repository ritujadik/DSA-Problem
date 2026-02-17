def prime_number(x):
    if x<= 1:
        return "Not a prime number",x
    for i in range(2,x):
        if x%i == 0:
            return("this is not a prime number",x)


    return("this is a prime number",x)




x = 5
print(prime_number(x))





