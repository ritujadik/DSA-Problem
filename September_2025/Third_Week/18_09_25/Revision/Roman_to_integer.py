def roman_to_integer(x):
    new_x = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    sum = 0
    prev_val = 0
    for i in reversed(x):
        value = new_x[i]
        if value < prev_val:
            sum -= value
        else:
            sum+= value
            prev_val = value
    return sum
x = "XII"
print(roman_to_integer(x))