from random import uniform as rand
main_matrix = []


for i in range(7):
    local_matrix = []
    for j in range(7):
        local_matrix.append(round(rand(1, 100), 2)) #задаем матрицу
    main_matrix.append(local_matrix[:])

#-------------------------------------------------------------------

for i in main_matrix:
    print(i, '\n') #распечатаем матрицу
print('\n')
#-------------------------------------------------------------------


def neighbors(i, j):
    false_list = [7, -1]
    all_neighbors = [main_matrix[i + di][j + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di != 0 or dj != 0) and (i + di not in false_list and j + dj not in false_list)]
    return all_neighbors

count = 0
new_list = []
for i in main_matrix:
    average_list = []
    for j in i:
        value = neighbors(main_matrix.index(i), i.index(j))
        average_value = (sum(value) + j) / (len(value) + 1)
        average_list.append(round(average_value, 2))
    new_list.append(average_list)


print(new_list)