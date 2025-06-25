def pyramid_pattern(n):
    for i in range(1, n+1):  # Loop for each row
        # Print leading spaces for the pyramid shape
        for j in range(n-i):
            print(" ", end="")  # Print spaces to center the numbers

        # Print numbers from 1 to i
        for k in range(1, i+1):
            print(k, end="")  # Print numbers in the current row

        print()  # Move to the next line after printing the row

x = pyramid_pattern(10)
