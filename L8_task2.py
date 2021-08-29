# 2.	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class DivisionByZeroException(Exception):
    def __init__(self, message):
        self.message = message


def my_division(a, b):
    try:
        if b == 0:
            raise DivisionByZeroException('Division by zero!')
    except DivisionByZeroException as e:
        print(e)
    else:
        return a / b
    finally:
        print('Division is finished.')


print(my_division(1, 2))
print(my_division(5.0, 3))
print(my_division(5, 0))
