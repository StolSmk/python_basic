# 4.	Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение
# числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без
# встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
# более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    return x ** y

def my_func_2(x, y):
    result = 1
    for i in range(0, -y):
        result *= x
    return 1 / result

X = float(input('Input x: '))
Y = int(input('Input y: '))

print(f'Result 1 = {my_func_1(X, Y)}. Result 2 = {my_func_2(X, Y)}')
