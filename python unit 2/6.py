def initialize_matrix(rows, cols):
    "Initialize matrix with zeros"
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    "Print matrix in grid form"
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(A, B):
    "Add two matrices"
    rows, cols = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

def multiply_matrices(A, B):
    "Multiply two matrices"
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix multiplication not possible")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
