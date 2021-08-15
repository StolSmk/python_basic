# 5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

file_path = 'task5_file.txt'

def file_creator(path):
    try:
        with open(path, 'w') as writer:
            string = ''
            for number in range(4, 20, 4):
                string += str(number) + ' '
            string = string.rstrip()
            writer.write(string)
    except IOError:
        print('IOError')
    finally:
        print(f'Set of numbers: {string}')
        print('Creation of file is finished.')

def file_reader(path):
    try:
        with open(path, 'r') as reader:
            number_list = [float(element) for element in reader.readline().split(' ')]
            print(f'Sum of numbers is: {sum(number_list)}')
    except IOError:
        print('IOError.')
    finally:
        print('Analyze is finished.')

file_creator(file_path)
file_reader(file_path)