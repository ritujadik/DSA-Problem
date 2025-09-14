def binary_add_number(b1,b2):
    sum_binary = bin(int(b1,2) + int(b2,2))[2:]
    return sum_binary



b1 = "1010"
b2 = "1011"
print(binary_add_number(b1,b2))