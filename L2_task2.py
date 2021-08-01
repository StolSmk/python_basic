# 2.	Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
# использовать функцию input().

element = input('Input element of list. If element is -1, input is finished: ')
my_list = [element if element != "-1" else None]

while element != "-1":
    element = input('Input element of list. If element is -1, input is finished: ')
    if element != "-1":
        my_list.append(element)
    else:
        break

print(f'Original list is: {my_list}!')

i = 0

while i < len(my_list):
    if i + 1 != len(my_list):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i = i + 2

print(f'Modified list is: {my_list}!')
