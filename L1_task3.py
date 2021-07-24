#3.	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем
# 3 + 33 + 333 = 369.
user_number = 0
while int(user_number) == 0:
    user_number = input('Input integer number except "0": ')
    if user_number == '0':
        print('Your number is "0". Input other number!')
        continue

output_number = int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)

print(f'Output number is "{output_number}"!')