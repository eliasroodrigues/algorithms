"""
    Magic Square
    
    author: Elias Rodrigues

    Properties:
        -> magic constant: M = n(n^2 + 1)/2
        -> magic square of order 1 is trivial
        -> magic square of order 2 cannot be constructed

    Types of magic square:
        -> odd (n = 3,5,7,9,...)
        -> doubly even (multiple of 4 where n = 4,8,12,16,...)
        -> singly even (divisible by 2 but not by 4, n = 6, 10, 14, 18,...) -> [(n*4) + 2]
"""

"""
    Magic Square of odd order

    link: https://www.1728.org/magicsq1.htm
"""
def magic_square_odd(square, col, row, value, old_row, tam):
    if value > tam*tam:
        return square
    else:
        if col >= tam:
            col = 0
        elif col < 0:
            col = tam - 1
        if row < 0:
            row = tam - 1
        elif row >= tam:
            row = 0
        if square[row][col] == 0:
            square[row][col] = value
            magic_square_odd(square, col + 1, row - 1, value + 1, row, tam)
        else:
            magic_square_odd(square, col - 1, old_row + 1, value, old_row, tam)

"""
    Magic Square of double even order

    link: https://www.1728.org/magicsq2.htm
"""
def magic_square_double_even(tam):
    if tam % 4 != 0:
        return None
   
    square = [[(tam*y)+x+1 for x in range(tam)] for y in range(tam)]

    # Top Left
    for i in range(tam // 4):
        for j in range(tam // 4):
            square[i][j] = (tam * tam + 1) - square[i][j]

    # Top Right
    for i in range(tam // 4):
        for j in range(3 * (tam // 4), tam):
            square[i][j] = (tam * tam + 1) - square[i][j]

    # Bottom Left
    for i in range(3 * (tam // 4), tam):
        for j in range(tam // 4):
            square[i][j] = (tam * tam + 1) - square[i][j]

    # Bottom Right
    for i in range(3 * (tam // 4), tam):
        for j in range(3 * (tam // 4), tam):
            square[i][j] = (tam * tam + 1) - square[i][j]

    # Center
    for i in range(tam // 4, 3 * (tam // 4)):
        for j in range(tam // 4, 3 * (tam // 4)):
            square[i][j] = (tam * tam + 1) - square[i][j]

    return square

"""
    Magic Square of singly even order

    link: https://www.1728.org/magicsq3.htm
"""
def magic_square_singly_even(size):
    pass

"""
    Verify if the magic square is valid
"""
def verify_magic_square(square, tam):
    magic_number = (tam * ((tam**2) + 1)) // 2

    # Create a list for rows, columns and diagonals
    rows = [row[0:] for row in square[0:]]
    columns = zip(*rows)
    primary_diagonal = [square[i][i] for i in range(len(square))]
    secondary_diagonal = [square[i][len(square)-i-1] for i in range(len(square))]

    # Calculate the sums
    sums_rows = [sum(x for x in r) for r in rows]
    sums_columns = [sum(x for x in c) for c in columns]
    sum_primary_diagonal = [sum(x for x in primary_diagonal)]
    sum_secondary_diagonal = [sum(x for x in secondary_diagonal)]

    print("\nMaigc Number:", magic_number)
    print("Rows:", sums_rows, "\nColumns:", sums_columns)
    print("Primary Diagonal:", sum_primary_diagonal, "\nSecondary Diagonal:", sum_secondary_diagonal)
    print()

if __name__ == "__main__":
    print("Magic Square")

    square = None
    while True:
        size = int(input("Input the size of the disired magic square: "))

        if size % 2 != 0:
            square = [[0 for y in range(size)] for x in range(size)]
            magic_square_odd(square, size // 2, 0, 1, 0, size)
        elif size % 4 == 0:
            square = magic_square_double_even(size)
        elif size % 2 == 0 and size % 4 != 0:
            square = magic_square_singly_even(size)
        else:
            print("Invalid size.")

        if square != None:
            print()
            print(square)
            verify_magic_square(square, size)
   
