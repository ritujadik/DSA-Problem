# Python Program for nth Fibonacci number using formula

def fibonacci_number(n):
    if n <= 0:
        print("Incorrect Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)



print(fibonacci_number(10))