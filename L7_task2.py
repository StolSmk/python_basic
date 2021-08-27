# 2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V
# и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def consumption(self):
        return self.size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        self.__height = height

    def consumption(self):
        return self.__height * 2 + 0.3

    @property
    def height(self):
        print(f'Height is {self.__height} for {self}')
        return self.__height

    @height.setter
    def height(self, height):
        if height > 200:
            self.__height = 200
        else:
            self.__height = height

my_coat = Coat(52)
my_costume = Costume(180)

print(f'Consumption for the coat is {my_coat.consumption()}')
print(f'Consumption for the costume is {my_costume.consumption()}')

var = my_costume.height

my_costume.height = 210

print(f'Height for the costume is {my_costume.height}. Consumption is {my_costume.consumption()}')
