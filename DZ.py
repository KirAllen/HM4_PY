import random

class Matrix:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.matrix = Matrix.create_matrix(rows, columns)

    @staticmethod
    def create_matrix(count_rows: int, count_colums: int) -> list[list]:
        new_matrix = []
        for i in range(count_rows):
            row = []
            for j in range(count_colums):
                row.append(random.randint(1,9))
            new_matrix.append(row)
        return new_matrix

    def transp (self):
        for column in range(self.columns):
            new_row = []
            for row in range(self.rows):
                new_row.append(self.matrix[row][column])
            self.matrix.append(new_row)
        for i in range(self.rows):
            self.matrix.pop(0)

    def __str__(self):
        output = ""
        for row in self.matrix:
            for num in row:
                output += f'{num:^3}'
            output += '\n'
        return output

rows, columns = map(int, input("Enter rows and columns: ").split())

matrix = Matrix(rows, columns)


print(f'Исходня Матрица:')
print(matrix)

print('________________________________________')
matrix.transp()

print(f'Транспонированная Матрица:')
print(matrix)


