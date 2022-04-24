"""
    Magic Square
    

    Properties:
        -> magic constant: M = n(n^2 + 1)/2
        -> magic square of order 1 is trivial
        -> magic square of order 2 cannot be constructed
"""

def magic_square(square, col, row, value, old_row, tam):
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
            magic_square(square, col + 1, row - 1, value + 1, row, tam)
        else:
            magic_square(square, col - 1, old_row + 1, value, old_row, tam)

def verify_magic_square(square, tam):
    # The value for the sum of rows and columns
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

    print("Rows:", sums_rows, "Columns:", sums_columns)
    print("Primary Diagonal:", sum_primary_diagonal, "Secondary Diagonal:", sum_secondary_diagonal)

if __name__ == "__main__":
    print("Magic Square")
    tam = 9
    square = [[] for x in range(tam)]
    for i in range(tam):
        for j in range(tam):
            square[i].insert(j, 0)
    magic_square(square, tam // 2, 0, 1, 0, tam)
    print(square)
    verify_magic_square(square, tam)
