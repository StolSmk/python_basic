# 1.	Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных будет свидетельствовать пустая строка.

try:
    with open('task1_file.txt', 'w') as file_writer:
        while True:
            input_string = input('Input string: ')
            if input_string != '':
                file_writer.write(input_string + '\n')
            else:
                print(f'Input finished.')
                break
except IOError:
    print(f'IOError.')



