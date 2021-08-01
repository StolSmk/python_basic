# 3.	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

my_list = ['winter', 'spring', 'summer', 'autumn']

month = input('Input number of month: ')

if month in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
    if month in ('3', '4', '5'):
        print(f'Season is: {my_list[1]}')
    elif month in ('6', '7', '8'):
        print(f'Season is: {my_list[2]}')
    elif month in ('9', '10', '11'):
        print(f'Season is: {my_list[3]}')
    else:
        print(f'Season is: {my_list[0]}')
else:
    print('Not number of month!')


my_dict = {'winter':['1', '2', '12'], 'spring':['3', '4', '5'], 'summer':['6', '7', '8'], 'autumn':['9', '10', '11']}

if month in sum(my_dict.values(), []):
    for key, value in my_dict.items():
        if month in value:
            print(f'Season is: {key}')
            break
else:
    print('Not number of month!')
