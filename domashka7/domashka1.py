class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.sum_matrix = []

    def __str__(self):
        line_matrex = ""
        for el_list in  self.matrix:
            line_matrex =line_matrex + "\n"
            for el in el_list:
                line_matrex = line_matrex + f"{el} "
        return line_matrex

    def __add__(self, other):
        if(len(self.matrix) != len(other.matrix)):
           raise ValueError
        for i in range(len(self.matrix)):
            ls = []
            for j in range(len(self.matrix[0])):
                ls.append(self.matrix[i][j] + other.matrix[i][j])
            self.sum_matrix.append(ls)
        return Matrix(self.sum_matrix)


m = Matrix([[1,2,20], [2,3,34], [4, 5,34]])
m2 = Matrix([[1,2,20], [2,3,34], [4, 5,34]])
m3 = Matrix([[1,2,20], [2,3,34], [4, 5,34]])
print(f"Первая матрица: {m}")
print(f"Вторая матрица: {m2}")
print(f"Третия матрица: {m3}")
print(f"Результат сложения двух: {m + m2 + m3}")

