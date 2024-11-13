import math
import numpy as np

# First Quesion
def restore_matrix(upper_triangle):
    # Определяем размер матрицы
    n = int((math.sqrt(8 * len(upper_triangle) + 1) - 1) / 2)
    matrix = [[0] * n for _ in range(n)]
    
    # Заполняем верхний треугольник матрицы
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]
            index += 1
    
    # Печатаем восстановленную матрицу по строкам
    for row in matrix:
        print(row)

upper_triangle = [1, 2, 3, 4, 5, 6] # Примерная матрица
restore_matrix(upper_triangle)
def process_matrix(matrix):
    # Извлечение диагональных элементов
    diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
    # Вычисление следа матрицы
    trace = sum(diagonal_elements)
    # Преобразование матрицы
    for i in range(len(matrix)):
        if i % 2 == 0:  # четные строки
            matrix[i] = [elem / trace for elem in matrix[i]]
    # Печать результатов
    print("Одномерный массив диагональных элементов:", diagonal_elements)
    print("След матрицы:", trace)
    print("Преобразованная матрица:")
    for row in matrix:
        print(row)
# Пример использования
matrix = [
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
]

process_matrix(matrix)