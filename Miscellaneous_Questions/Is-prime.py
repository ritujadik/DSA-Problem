def is_prime(number):
    for i in range(2,number-1):
        if number%i == 0:
            return(number,"This is not a prime number")

        else:
            return (number,"This is a prime number")


x = is_prime(4)
print(x)

