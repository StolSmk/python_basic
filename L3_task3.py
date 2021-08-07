# 3.	Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func(var_1, var_2, var_3):
    min_var = min((var_1, var_2, var_3))
    new_list = [var_1, var_2, var_3]
    new_list.remove(min_var)
    return sum(new_list)

Var_1 = float(input('Input 1 var: '))
Var_2 = float(input('Input 2 var: '))
Var_3 = float(input('Input 3 var: '))

print(f'Result is: {my_func(Var_1, Var_2, Var_3)}.')
