# 3.	Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def write(path):
    try:
        with open(path, 'w') as data_writer:
            while True:
                surname = input('Input surname: ')
                if surname != '':
                    salary = input('Input salary: ')
                    data_writer.write(surname + ' ' + salary + '\n')
                else:
                    break
    except IOError:
        print('IOError.')

def reader(path):
    try:
        with open(path, 'r') as data_reader:
            staff = {list(string.split())[0] : float(list(string.split())[1]) for string in data_reader if
                     float(list(string.split())[1]) < 20000}
            print(f'Poor staff: {staff.keys()}')
            print(f'Average salary: {sum(staff.values()) / len(staff.values())}')
    except IOError:
        print(f'IOError.')

# write('task3_file.txt')
reader('task3_file.txt')