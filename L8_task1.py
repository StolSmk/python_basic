# 1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-
# год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date():
    __date = None

    def __init__(self, date):
        Date.__date = date

    @classmethod
    def conversion(cls):
        try:
            list_of_date = list(map(int, list(str(cls.__date).split('-'))))
            # return [int(el) for el in str(cls.date).split('-')]
        except ValueError as e:
            print(f'Incorrect format of date. Exception: {e.__str__()}')
        else:
            return list_of_date
            print(f'List of date: {list_of_date}')
        finally:
            print(f'Conversion is finished.')

    @staticmethod
    def validation(list_of_date):
        try:
            days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            if list_of_date[2] >= 0:
                print(f'Year {list_of_date[2]} is correct')
            else:
                print(f'Year {list_of_date[2]} is incorrect')
            if 0 < list_of_date[1] <= 12:
                print(f'Month {list_of_date[1]} is correct')
                if 0 < list_of_date[0] <= days_in_month[list_of_date[1] + 1]:
                    print(f'Day {list_of_date[0]} is correct')
                else:
                    print(f'Day {list_of_date[0]} is incorrect')
            else:
                print(f'Month {list_of_date[1]} is incorrect')
                print(f'Day {list_of_date[0]} is incorrect')
        except TypeError as e:
            print(f'Incorrect format of date. Exception: {e.__str__()}')
        else:
            pass
        finally:
            print(f'Validation is finished.')


my_date_1 = Date('25-08-2021')
Date.validation(my_date_1.conversion())
print()
my_date_2 = Date('35-18-0')
Date.validation(my_date_2.conversion())
print()
my_date_3 = Date('a35-18t-f0')
Date.validation(my_date_2.conversion())
