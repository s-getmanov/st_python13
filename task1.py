import random

def printMatrix(matrix):
    for i in matrix:
        print(*i)

def inputMatrixSize():
    ls = []      
    err = ""
    while len(ls) < 2 or ls[0] < 1 or ls[1] < 1:
        if err:
            print(err)
        ls = list(map(int, input(f"Введите размер матриц (два положительных числа через пробел):").split())) 
        err = "Неверный ввод!"       
    return (ls[0], ls[1])

def generateMatrix(size, randomData):
    matrix = []
    for i in range(size[0]):
        matrixIn = []
        for j in range(size[1]):
            if randomData:
                matrixIn.append(random.randint(1, 100))
            else:    
                matrixIn.append(0)
        matrix.append(matrixIn)
    return matrix

def matrixSumm(matrix1, matrix2, matrix_size):

    matrix_result = generateMatrix(matrix_size, False)

    for i in range(0,matrix_size[0]):
       for j in range(0, matrix_size[1]):
           matrix_result[i][j] = matrix1[i][j] + matrix2[i][j]           
    return matrix_result

matrix_size = inputMatrixSize()
matrix1 = generateMatrix(matrix_size, True)
matrix2 = generateMatrix(matrix_size, True)
summ_matrix = matrixSumm(matrix1, matrix2, matrix_size)

print("Матрица 1:")
printMatrix(matrix1)
print()
print("Матрица 2:")
printMatrix(matrix2)
print()
print("Результат сложения матриц:")
printMatrix(summ_matrix)
print()


