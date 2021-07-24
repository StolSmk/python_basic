#4.	Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.
input_number = int(input('Input integer positive number: '))
max_number = 0
i = 0
while (input_number // (10 ** i)) != 0:
    if max_number < ((input_number // (10 ** i)) % 10):
        max_number = ((input_number // (10 ** i)) % 10)
    i += 1

print(f'The maximum digit is "{max_number}"!')