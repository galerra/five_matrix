'''
 Характеристикой строки целочисленной матрицы назовем сумму ее положительных четных элементов.
 Переставляя строки заданной матрицы, расположить их в соответствии с ростом характеристик.
'''

array_var = [[4, 5, 6],
             [7, 8, 9],
             [1, 2, 3]]
array_var_new = []
array_sum = []

for i in array_var:
    count = 0
    for j in i:
        if j > 0 and j % 2 == 0:
            count += j
    array_sum.append(count)

for i in range(len(array_sum)):
    array_var_new.insert(0, array_var[array_sum.index(max(array_sum))])
    array_var.pop(array_sum.index(max(array_sum)))
    array_sum.remove(max(array_sum))
print(array_var_new)