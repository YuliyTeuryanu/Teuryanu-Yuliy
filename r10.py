import math


with open('Тэуряну Юлий Владимирович_У-243_vvod.txt', 'r') as fl:
    lines = fl.readlines()

matrix = []
for line in lines:
    cl = line.replace('[', '').replace(']', '').replace(',', '').strip()
    if cl: 
        row = list(map(int, cl.split()))
        matrix.append(row)

def restore_matrix(upper_triangle):
    
    n = int((math.sqrt(8 * len(upper_triangle) + 1) - 1) / 2)
    matrix = [[0] * n for _ in range(n)]
    
    
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]
            index += 1
    
    return matrix  

def process_matrix(matrix):
    diagonal_elements = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    
    trace = sum(diagonal_elements)
    
    for i in range(len(matrix)):
        if trace != 0 and i % 2 != 0:  
            matrix[i] = [elem / trace for elem in matrix[i]]
    
    return matrix  
upper_triangle = [matrix[i][j] for i in range(len(matrix)) for j in range(i, len(matrix))]
restored_matrix = restore_matrix(upper_triangle)
result_matrix = process_matrix(restored_matrix)
with open('Тэуряну Юлий Владимирович_У-243_vivod.txt', 'w') as fl:
    for row in result_matrix:
        fl.write(' '.join(map(str, sorted(row))) + "\n")



