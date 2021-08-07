# 5.	Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
# введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def my_sum(input_string):
    result = str(input_string).split()
    if 'stop' not in result:
        for i, element in enumerate(result):
            result[i] = int(element)
    else:
        result.remove('stop')
        for i in range(0, len(result)):
            result[i] = int(result[i])
    return sum(result)

sum_result = 0

input_data = input('Input data: ')

while 'stop' not in str(input_data).split():
    sum_result += my_sum(input_data)
    print(f'Current result is: {sum_result}.')
    input_data = input('Input data: ')

sum_result += my_sum(input_data)
print(f'Current result is: {sum_result}. STOP')
