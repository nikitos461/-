import numpy as np
def cramer_method(matrix, vector):
    if not (matrix.shape[0] == matrix.shape[1]):
        return None   
    n = len(matrix)
    det_A = np.linalg.det(matrix)
    if dat_A == 0:
        return None
    solutions = []
    for i in range(n):
        A_i = matrix.copy()  # замена столбца на свободные члены
        A_i[:, i] = vector
        
        det_i = np.linalg.det(A_i) # определитель после замены
        solutions.append(det_i / det_A) # добавление решения после замены
    return solutions


# Сюда вводить матрицу!!! 
A = np.array([[5, -3], [2, 3]])  # Матрица коэффициентов
B = np.array([17, 11])          # Вектор свободных членов
solution = cramer_method(A, B)
print(solution)


#Если код переводится автоматически на русский, то нужно скачивать .py файл
#Также, скорее всего из-за того, что идет работа с числами с плавающей точкой, получается какая-то погрешность
#В связи с чем результаты получаются не точными, а максимально приближенными ¯\_(ツ)_/¯
