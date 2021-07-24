"""
1.	Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
и сохраните в переменные, затем выведите на экран.
"""
number = 1
string_1 = "My 'string' one."
string_2 = 'My "string" two.'
boolean = True
print(f'The number is "{number}".\nThe first string is "{string_1}".\nThe second string is "{string_2}".\nThe boolean '
      f'variable is "{boolean}".')

var_int = int(input("Input integer number: "))
print(f'Your integer number is "{var_int}"!')
var_float = float(input("Input floating point number: "))
print(f'Your floating point number is "{var_float}"!')
var_bool = bool(input("Input bool value: "))
print(f'Your bool value is "{var_bool}"!')
var_string = input("Input string value: ")
print(f'Your string value is "{var_string}"!')

