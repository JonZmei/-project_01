class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(cols)] for i in range(rows)]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def replace_value(self, row, col, value):
        if self.matrix[row][col] is not None:
            self.matrix[row][col] = value

    def get_num_rows(self):
        return self.rows

    def get_num_cols(self):
        return self.cols

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])



# Создаем матрицу 10 на 10 из единиц
matrix = Matrix(10, 10)
for i in range(matrix.get_num_rows()):
    for j in range(matrix.get_num_cols()):
        matrix.set_value(i, j, 1)

print(matrix)  # Выводим матрицу

# Пример замены значения в ячейке
matrix.replace_value(0, 0, 2)
print(matrix)
