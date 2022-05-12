import math
list_variable = list(map(int, input().split()))


class Matrix:
    def __init__(self, quantity_string=None, square_matrix=None, rectangular_matrix=None):
        self.quantity_string = quantity_string
        self.list_variable = list_variable
        self.square_matrix = square_matrix
        self.rectangular_matrix = rectangular_matrix

    def convert_to_rectangular_matrix(self):
        global rectangular_matrix
        rectangular_matrix = []
        matrix_size = len(list_variable)
        column = 0
        count = 0
        intermediate_list = []
        for i in range(2, matrix_size):
            if matrix_size % i == 0:
                column = i
        if column != 0:
            for i in list_variable:
                intermediate_list.append(i)
                count += 1
                if count == column:
                    rectangular_matrix.append(intermediate_list[:])
                    intermediate_list.clear()
                    count = 0
            return rectangular_matrix
        else:
            return 'Sorry, you entered the wrong number of elements'

    def convert_to_triangle_matrix(self):
        triangle_matrix = []
        intermediate_list = []
        max_count_num = 0
        matrix_size = len(rectangular_matrix) * len(rectangular_matrix[0])
        while max_count_num < matrix_size:
            matrix_size -= max_count_num
            max_count_num += 1
        combo_list = []
        for i in rectangular_matrix:
            combo_list += i
        count = 1
        n = 0
        for i in range(max_count_num):
            slice = combo_list[0:i + 1]
            triangle_matrix.append(slice)
            combo_list = combo_list[i + 1:]
            null_count = max_count_num - count
            for _ in range(null_count):
                slice.append(0)
            count += 1
        return triangle_matrix






matrix = Matrix()
print(matrix.convert_to_rectangular_matrix())
print(matrix.convert_to_triangle_matrix())

