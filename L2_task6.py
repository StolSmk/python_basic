# 6.	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть
# характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например,
# название. Тогда значение — список значений-характеристик, например, список названий товаров.
#
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

goods = []
i = 1
input_name = None
input_price = None
input_amount = None
input_unit = None

while input_name or input_price or input_amount or input_unit != '':
    print(f'good number {i}:')
    input_name = input('Input name: ')
    input_price = input('Input price: ')
    input_amount = input('Input amount: ')
    input_unit = input('Input unit: ')
    if input_name or input_price or input_amount or input_unit != '':
        goods.append((i, {"name":input_name, "price":input_price, "amount":input_amount, "unit":input_unit}))
        i = i + 1

print(goods)

names = []
prices = []
amounts = []
units = []

for element in goods:
    names.append(element[1].get('name'))
    prices.append(element[1].get('price'))
    amounts.append(element[1].get('amount'))
    units.append(element[1].get('unit'))

statistic = {'names':names, 'prices':prices, 'amounts':amounts, 'units':units}

print(statistic)


