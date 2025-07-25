# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

"""
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR" """

"""
Plan of action
1.We need to know how many rows are there 
2.We will traverse vertically downward upto number of rows
3.then will traverse upward by nuober of rows -2 in a reverse order
4. will follow the step 2 and 3 up to length of string
5. then print the rows by using .join method
"""
# code
def zigzag(s,r):
    if r == 1 or r >= len(s):
        return s
    result = ['' for i in range(r)]
    goes_down = True
    current_row = 0
    for char in s:
        result[current_row]+=char
        if current_row == 0:
            goes_down = True
        elif current_row == r-2:
            goes_down = False
        current_row+=1 if goes_down else -1
    return (''.join(result))

z=zigzag("AB",1)
print(z)