# 7.	Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(word):
    return str(word).title()

input_string = input('Input string: ')

result = ''

for element in str(input_string).split():
    result += int_func(element) + ' '

print(f'Result is: {result}')
