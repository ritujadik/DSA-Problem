def zigzag(s,num_of_rows):
    if num_of_rows ==1 or num_of_rows>=len(s):
        return s

    result = ['' for _ in range(num_of_rows)]
    current_row = 0
    going_down = False

    for char in s:
        result[current_row]+=char

        if current_row == 0:
            going_down = True

        elif current_row == num_of_rows-1:
            going_down = False

        current_row+=1 if going_down else -1

    return ''.join(result)



s = "PAYPALISHIRING"
num_of_rows = 3
x = zigzag(s,num_of_rows)
print(x)

