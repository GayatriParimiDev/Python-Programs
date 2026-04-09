
def print_matrix(m):
    for row in m:
        print(row)

def add_matrix(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiply_matrix(a, b):
    result = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k]*b[k][j]
    return result
