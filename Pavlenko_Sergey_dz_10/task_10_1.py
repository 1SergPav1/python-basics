# Задание 1

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.data])

    def __add__(self, other):
        sum_matrix = []
        if len(self.data) == len(other.data):
            for line1, line2 in zip(self.data, other.data):
                if len(line1) != len(line2):  # проверка матриц на одинаковую размерность
                    return 'матрицы должны быть одинаковой размерности'
                sum_line = [x + y for x, y in zip(line1, line2)]
                sum_matrix.append(sum_line)
        else:
            return 'матрицы должны быть одинаковой размерности'
        return Matrix(sum_matrix)


a = [[1, 2, 9], [3, 4, 1], [5, 6, 1]]
b = [[7, 4, 1], [1, 1, 2], [5, 2, 7]]

matrix1 = Matrix(b)
print(matrix1)
print('-' * 8)
matrix2 = Matrix(a)

print(matrix1 + matrix2)
