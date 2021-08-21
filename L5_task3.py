# 3.	Реализовать базовый класс Worker (работник).
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    __income_of_worker = {'wage': 10000, 'bonus': 50000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = Worker.__income_of_worker

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

new_position = Position('Alex','Smith','Position_1')
print(f'Position: {new_position.position}')
print(f'Full name: {new_position.get_full_name()}')
print(f'Total income: {new_position.get_total_income()}')

