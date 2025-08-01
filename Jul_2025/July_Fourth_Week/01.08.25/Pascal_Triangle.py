"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
"""

#Approach
#1.In this question we are given a number of rows that represent how many rows are generate in pascal triangle.
#2.we will take empty list name is triangle to store the result.
#3. we will loop from 0 to numrows-1
#4.for each iteration 'i' we will initialize a row list of length(i+1) filled with 1's.
#5.we will iterate from index 1 to i-1 to fill the inner elements of the row
#6.each inner element of index 'j' is calculated as:
#           row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#7.after constructing the row we will append the 'triangle'list.
#8.after a loop we will return a triangle

def pascal_triangle(num_of_rows):
    triangle = []
    for i in range(num_of_rows):
        row = [1] * (i+1)

        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


print(pascal_triangle(5))