# Python Program to Check Armstrong Number

def check_armstrong_number(x):
    x_str = str(x)
    x1 = len(x_str)
    sum_of_powers = sum(int(digit) ** x1 for digit in x_str)

    return sum_of_powers == x



print(check_armstrong_number(153))