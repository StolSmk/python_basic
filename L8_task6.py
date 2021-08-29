# 6.	Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class IsNotDigitException(Exception):
    def __init__(self, message):
        pass


class OfficeEquipmentStorage():
    def __init__(self):
        self.__office_equipment = {}
        self.__office_equipment_in_departments = {}

    @property
    def office_equipment(self):
        print('Here is dictionary with equipment.')
        return self.__office_equipment

    @property
    def office_equipment_in_departments(self):
        print('Equipment in departments.')
        return self.__office_equipment_in_departments

    def add_equipment(self, new_equipment):
        list_equipment = self.__office_equipment.setdefault(new_equipment.type_epuipment)
        if list_equipment is None:
            self.__office_equipment[new_equipment.type_epuipment] = [new_equipment]
        else:
            self.__office_equipment[new_equipment.type_epuipment].append(new_equipment)

    def send_equipment_to_department(self, department, equipment):
        all_equipment = []
        for el in self.__office_equipment.values():
            all_equipment += el
        if equipment in all_equipment:
            list_equipment = self.__office_equipment_in_departments.setdefault(department)
            if list_equipment is None:
                self.__office_equipment_in_departments[department] = [equipment]
            else:
                self.__office_equipment_in_departments[department].append(equipment)
            self.__office_equipment[equipment.type_epuipment].remove(equipment)
        else:
            print('No such equipment.')

    def input_equipment(self):
        input_type = input('Input type: ')
        input_id = input('Input id: ')
        input_speed = input('Input speed: ')
        try:
            if not input_speed.replace('.', '', 1).isdigit():
                raise IsNotDigitException('Is not digit.')
        except IsNotDigitException as e:
            print(e)
        else:
            if input_type == Printer.__name__:
                self.add_equipment(Printer(input_id, input_speed))
            elif input_type == Scanner.__name__:
                self.add_equipment(Scanner(input_id, input_speed))
            else:
                print('Such type is absent.')


class OfficeEquipment():
    def __init__(self, type_epuipment, serial_id):
        self.type_epuipment = type_epuipment
        self.serial_id = serial_id

    def __str__(self):
        return f'Type: {self.type_epuipment}, serial ID: {self.serial_id}'

    def __repr__(self):
        return f'(Type: {self.type_epuipment}, serial ID: {self.serial_id})'


class Printer(OfficeEquipment):
    def __init__(self, serial_id, printing_speed):
        self.type_epuipment = 'Printer'
        self.serial_id = serial_id
        self.printing_speed = printing_speed


class Scanner(OfficeEquipment):
    def __init__(self, serial_id, scanning_speed):
        self.type_epuipment = 'Scanner'
        self.serial_id = serial_id
        self.scanning_speed = scanning_speed


my_storage = OfficeEquipmentStorage()
my_storage.input_equipment()
print(my_storage.office_equipment)