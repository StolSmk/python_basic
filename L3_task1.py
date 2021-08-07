# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(var_1, var_2):
    if var_2 == 0:
        print('Error: "division by zero"! Input again.')
    else:
        return var_1 / var_2

dividend = float(input('Input dividend: '))
divisor = float(input('Input divisor: '))

result = division(dividend, divisor)

while result is None:
    if result is None:
        dividend = float(input('Input dividend: '))
        divisor = float(input('Input divisor: '))
        result = division(dividend, divisor)

print(f'Quotient is: {result}.')