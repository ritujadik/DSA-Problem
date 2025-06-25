def matrixfun(lst,row,col):
    matrix = []
    if len(lst) != row*col:
        return ("this matrix cannot be formed as row*col is not equal to total elmement")
    else:
        for i in range(0,len(lst),col):
            matrix.append(lst[i:i +col])

        matrixtransform = []
        for j in range(col):
            transformed_row =[]
            for k in range(row):
                transformed_row.append(matrix[row -1 -k][j])
            matrixtransform.append(transformed_row)

        return matrixtransform




lst = [1,2,3,4,5,6,7,8,9]
x = matrixfun(lst, 3, 3)
for i in x:
    print(i)


