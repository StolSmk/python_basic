# 2.	Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить
# вывод данных о пользователе одной строкой.

def user_data(name, surname, year_of_birth, current_city, email, phone_number):
    print(f'name is: {name}; surname is: {surname}; year of birth is: {year_of_birth}; current city is: {current_city};'
          f' email is: {email}; phone number is: {phone_number}')

Name = input('Input name: ')
Surname = input('Input surname: ')
Year_or_birth = input('Input year: ')
Current_city = input('Input city: ')
Email = input('Input email: ')
Phone_number = input('Input phone: ')

user_data(name=Name, surname=Surname, year_of_birth=Year_or_birth, current_city=Current_city, phone_number=Phone_number,
          email=Email)
