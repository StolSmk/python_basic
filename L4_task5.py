# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def form_list(a, b):
    return [el for el in range(a, b + 1) if el % 2 == 0]

print(f'List is: {form_list(100, 1000)}.')

print(f'Product is: {reduce(lambda x, y: x * y, form_list(100, 1000))}')

res = 1

my_list = form_list(100, 1000)

for i in range(0, len(my_list)):
    res *= my_list[i]

print(f'Product is: {res}')
