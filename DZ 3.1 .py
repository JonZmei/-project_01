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

# Вот например вариант со словарями в качетсве строк
class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])



table1 = Table([1, 2])
table1.add_row({1: 10, 2: 20})
table1.add_row({1: 20, 2: 400})
table1.add_row({1: 30, 2: 600})
table1.add_row({1: 40, 2: 800})
print(table1.get_column(1))
print(table1.get_column(2))
print(table1.rows)
