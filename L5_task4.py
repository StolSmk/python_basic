# 4.	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
dict_mapping = { 'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

def data_reader_writer(path):
    new_path = path.split('.')[0] + '_1.' + path.split('.')[1]
    try:
        with open(path, 'r', encoding='utf-8') as data_r:
            list_data = [[string.rstrip().split(' — ')[0], string.rstrip().split(' — ')[1]] for string in data_r]
            for element in list_data:
                if element[0] in dict_mapping.keys():
                    element[0] = dict_mapping[element[0]]
        with open(new_path, 'w') as data_w:
            for element in list_data:
                data_w.write(f'{element[0]} - {element[1]}\n')
    except IOError:
        print('IOError.')
    finally:
        print('Finished.')

data_reader_writer('task4_file.txt')
