"""
check if given number is prime
"""

def prime_number(x):
    for i in range(2,x-1):
        if x % i != 0:
            return("this is a prime number",{x})
        else:
            return ("this is not a prime number", {x})


x = 17
print(prime_number(x))