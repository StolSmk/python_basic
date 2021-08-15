# 7.	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

file_path = 'task7_file.txt'
json_file_path = 'task7_file.json'

def list_creator(path):
    try:
        with open(path, 'r') as reader:
            dict_data = {string.split()[0]: float(string.split()[2]) - float(string.split()[3]) for string in reader}
            profit_firms = [profit for profit in dict_data.values() if profit >= 0]
            average_profit = sum(profit_firms)/len(profit_firms)
            list_result = [dict_data, {'average_profit': average_profit}]
            print(list_result)
            return list_result
    except IOError:
        print('IOError')
    finally:
        print('Creation of list is finished.')

def json_creator(path_text, path_json):
    try:
        with open(path_json, 'w') as writer:
            json.dump(list_creator(path_text), writer)
    except IOError:
        print('IOError.')
    finally:
        print('Serialization is finished.')


json_creator(file_path, json_file_path)