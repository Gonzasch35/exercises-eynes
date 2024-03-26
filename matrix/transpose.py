def transpose(matrix):
    
    filas = len(matrix)
    columnas = len(matrix[0])

    matrix_transpuesta = [[0] * filas for n in range(columnas)]

    for i in range(filas):
            for j in range(columnas):
                matrix_transpuesta[j][i] = matrix[i][j]

    return matrix_transpuesta