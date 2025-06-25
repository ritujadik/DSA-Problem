def spiralmatr(matrix):
    result = []

    if not matrix:
        return result

    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix)-1

    while top <= bottom and left <= right:

        for i in range(left,right + 1):
            result.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left -1,-1):
                result.append(matrix[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result


matrix = [
          [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
]
x = spiralmatr(matrix)
print(x)
