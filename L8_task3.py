# 3.	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
# экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
# пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.


class IsNotDigitException(Exception):
    def __init__(self, message):
        pass


class CorrectDigitListInput():
    def __init__(self):
        self.__list_of_digits = []

    def do_list_input(self):
        input_data = input('Input digit: ')
        while input_data != 'stop':
            try:
                if not input_data.replace('.', '', 1).isdigit():
                    raise IsNotDigitException('Is not digit.')
            except IsNotDigitException as e:
                print(e)
            else:
                self.__list_of_digits.append(float(input_data))
            input_data = input('Input digit: ')
        print(f'Result list of digits is: {self.__list_of_digits}')


my_list = CorrectDigitListInput()
my_list.do_list_input()




