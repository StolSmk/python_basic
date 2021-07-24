#2.	Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
input_data = int(input('Input time in seconds: '))
hours = input_data // (60 ** 2)
minutes = (input_data % (60 ** 2)) // 60
seconds = (input_data % (60 ** 2)) % 60
print(f'Time in "hh:mm:ss" - format is "{hours}:{minutes}:{seconds}"!')