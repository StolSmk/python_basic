# 4.	Реализуйте базовый класс Car.
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'{self.name} goes.')

    def stop(self):
        print(f'{self.name} stopped.')

    def turn(self, direction):
        print(f'{self.name} turned {direction}.')

    def show_speed(self):
        print(f'Speed of {self.name} is {self.speed}.')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed of {self.name} is {self.speed}. Over speed!')
        else:
            print(f'Speed of {self.name} is {self.speed}.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed of {self.name} is {self.speed}. Over speed!')
        else:
            print(f'Speed of {self.name} is {self.speed}.')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

town_car_1 = TownCar(70, 'green', 'town_car_1')
town_car_2 = TownCar(50, 'green', 'town_car_2')
work_car_1 = WorkCar(70, 'white', 'work_car_1')
sport_car_1 = SportCar(110, 'red', 'sport_car_1')
police_car_1 = PoliceCar(120, 'black', 'police_car_1')

print(f'{town_car_1.name} with color: {town_car_1.color} have speed: {town_car_1.speed}. Is police: {town_car_1.is_police}')
print(f'{police_car_1.name} with color: {police_car_1.color} have speed: {police_car_1.speed}. Is police: {police_car_1.is_police}')
town_car_1.show_speed()
town_car_2.show_speed()
work_car_1.show_speed()
sport_car_1.go()
sport_car_1.turn('Right')
police_car_1.go()
sport_car_1.stop()
police_car_1.stop()