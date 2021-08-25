# 1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list):
        self.__matrix_list = matrix_list

    def __str__(self):
        result = ''
        for row in self.__matrix_list:
            for el in row:
                result += str(el) + '\t'
            result += '\n'
        return result

    def __add__(self, other):
        result = []
        i = 0
        j = 0
        for i in range(0, len(self.__matrix_list)):
            row = []
            for j in range(0, len(self.__matrix_list[i])):
                row.append(self.__matrix_list[i][j] + other.__matrix_list[i][j])
            result.append(row)
        return Matrix(result)

my_matrix_1 = Matrix([[1, 1, 1], [1, 1, 1]])
my_matrix_2 = Matrix([[2, 2, 2], [2, 2, 2]])

print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_1 + my_matrix_2)
