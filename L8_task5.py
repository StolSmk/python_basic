# 5.	Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру (например, словарь).


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


my_printer_1 = Printer('001', 100)
my_printer_2 = Printer('002', 110)

my_scanner_1 = Scanner('001', 100)
my_scanner_2 = Scanner('002', 90)

print(str(my_printer_1) + '; ' + str(my_printer_2) + '; ' + str(my_scanner_1) + '; ' + str(my_scanner_2))

my_storage = OfficeEquipmentStorage()
my_storage.add_equipment(my_printer_1)
my_storage.add_equipment(my_printer_2)
my_storage.add_equipment(my_scanner_1)
my_storage.add_equipment(my_scanner_2)

print(my_storage.office_equipment)

my_storage.send_equipment_to_department('Bookkeeping', my_printer_1)

print(my_storage.office_equipment)
print(my_storage.office_equipment_in_departments)

my_storage.send_equipment_to_department('Bookkeeping', Printer('90', 200))

print(my_storage.office_equipment)
print(my_storage.office_equipment_in_departments)
