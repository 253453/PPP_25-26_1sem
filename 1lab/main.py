import random


n = random.randint(2, 10)   
m = random.randint(2, 10) 

matrix = [] 

for i in range(n): 
    row = [] 
    for j in range(m): 
        row.append(random.randint(0, 100)) 
    matrix.append(row) 

for i in range(n): 
    for j in range(m): 
        print(f'{matrix[i][j]:3}', end=' ') 
    print() 

row_maxx = [] 

for i in range(n): 
    row_max = matrix[i][0]  
    for j in range(1, m): 
        if matrix[i][j] > row_max: 
            row_max = matrix[i][j] 
    row_maxx.append(row_max) 

column_maxx = [] 

for j in range(m): 
    column_max = matrix[0][j]  
    for i in range(1, n): 
        if matrix[i][j] > column_max: 
            column_max = matrix[i][j] 
    column_maxx.append(column_max) 

main_diag_sum = 0 
secondary_diag_sum = 0 

for i in range(min(n, m)): 
    main_diag_sum += matrix[i][i] 
    secondary_diag_sum += matrix[i][m - 1 - i] 
max_sum = sum(matrix[0]) 
max_row_index = 0 

for i in range(1, n): 
    current_sum = sum(matrix[i]) 
    if current_sum > max_sum: 
        max_sum = current_sum 
        max_row_index = i 

print('\nМаксимумы по строкам:')
for i in range(n):
    print(f'Строка {i}: {row_maxx[i]}')

print('\nМаксимумы по столбцам:')
for j in range(m):
    print(f'Столбец {j}: {column_maxx[j]}')

print('\nСумма главной диагонали:',main_diag_sum)
print('\nСумма побочной диагонали:',secondary_diag_sum)

print('\nСтрока с наибольшей суммой:',max_row_index,',', 'Сумма = ',max_sum)

