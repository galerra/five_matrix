import math
list_variable = list(map(int, input().split()))


def convert_to_square_matrix(list_variable):
        square_matrix = []
        intermediate_list = []
        count = 0
        matrix_size = len(list_variable)
        if float(math.sqrt(matrix_size)) - int(math.sqrt(matrix_size)) == 0:
            for i in list_variable:
                intermediate_list.append(i)
                count += 1
                if count == math.sqrt(matrix_size):
                    square_matrix.append(intermediate_list[:])
                    intermediate_list.clear()
                    count = 0
        else:
            return 'Square: cannot be converted'
        return square_matrix

count_diag_val = len(convert_to_square_matrix())
new_list_variable = list_variable.copy()
new_list_variable.sort()
new_list_variable.reverse()
diagonal = new_list_variable[0:count_diag_val]
print(diagonal)
print(convert_to_square_matrix())


for i in range(count_diag_val):
    value = diagonal[i]
    list_variable[list_variable.index(value)], list_variable[i] = list_variable[i], list_variable[list_variable.index(value)]

print(convert_to_square_matrix(list_variable=list_variable))