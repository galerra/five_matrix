from random import randint as rand
main_matrix = []

#-------------------------------------------------------------------

for i in range(10):
    local_matrix = []
    for j in range(10):
        local_matrix.append(rand(1, 100)) #задаем матрицу
    main_matrix.append(local_matrix[:])

#-------------------------------------------------------------------

for i in main_matrix:
    print(i, '\n') #распечатаем матрицу
print('\n')
#-------------------------------------------------------------------


def neighbors(i, j):
    false_list = [10, -1]
    all_neighbors = [main_matrix[i + di][j + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di != 0 or dj != 0) and (i + di not in false_list and j + dj not in false_list)]
    return all_neighbors

count = 0

for i in main_matrix:
    for j in i:
        value = neighbors(main_matrix.index(i), i.index(j))
        value.sort()
        if j < value[0]:
            count += 1
print(count)
