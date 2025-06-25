def matrixfunc(lst,row,col):
    if len(lst) != row * col:
        return ("we wont be able to make a matrix")
    else:
        matrix = []
        for i in range(0,len(lst),col):
            matrix.append(lst[i:i + 3])

        matrix_transpose = []
        for j in range(col):
            transpose_row = []
            for k in range(row):
                transpose_row.append(matrix[k][-j -1])
            matrix_transpose.append(transpose_row)
        return matrix_transpose


lst = [1,2,3,4,5,6,7,8,9]
row = 3
col = 3
x = matrixfunc(lst,row,col)
for i in x:
    print(i)