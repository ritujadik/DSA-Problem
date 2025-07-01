# check whether the given number is prime or not

def prime_number(x):
    if x < 2:
        return "This is not a prime number"
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return ("This number not a prime number")
    return ("This is a prime number")

print(prime_number(4))
