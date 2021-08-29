# 7.	Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber():
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __repr__(self):
        return f'{self.re} + ({self.im})i'


print(ComplexNumber(1, 1) + ComplexNumber(2, 2))
print(ComplexNumber(1, 1) * ComplexNumber(2, 2))
print(ComplexNumber(1, 1))
