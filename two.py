'''
Для заданной матрицы размером 8 на 8 найти такие k,
что k -я строка матрицы совпадает с k-м столбцом.
'''

array_var = [
             [10, 20, 30, 40, 50, 60, 70, 80],
             [20, 10, 11, 26, 13, 14, 15, 16],
             [30, 18, 19, 27, 21, 22, 23, 24],
             [40, 26, 27, 28, 29, 30, 31, 32],
             [50, 34, 35, 29, 37, 38, 39, 40],
             [60, 42, 43, 30, 45, 46, 47, 48],
             [70, 50, 51, 31, 53, 54, 55, 56],
             [80, 58, 59, 32, 61, 62, 63, 65]
             ]

array_bank_k = []

for i in array_var:
    for j in range(0, 8):
        x = [x[j] for x in array_var]
        if x == i:
            array_bank_k.append(array_var.index(i) + 1)
print(array_bank_k)

