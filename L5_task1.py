# 1.	Создать класс TrafficLight (светофор).
# ●	определить у него один атрибут color (цвет) и метод running (запуск);
# ●	атрибут реализовать как приватный;
# ●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# ●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# ●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# ●	проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import perf_counter

class TrafficLight:
    def __init__(self, start_color = 'red'):
       print(f'Traffic light is created.')
       self.__color = start_color

    def running(self):
        if self.__color in ('red', 'yellow', 'green'):
            print(f'Traffic light is started.')
            if self.__color == 'red':
                print('red')
                self.__my_timer(7)
                print('yellow')
                self.__my_timer(2)
                print('green')
                self.__my_timer(3)
            elif self.__color == 'yellow':
                print('yellow')
                self.__my_timer(2)
                print('green')
                self.__my_timer(3)
                print('red')
                self.__my_timer(7)
            elif self.__color == 'green':
                print('green')
                self.__my_timer(3)
                print('red')
                self.__my_timer(7)
                print('yellow')
                self.__my_timer(2)
            print(f'Traffic light is finished.')
        else:
            print('Start color is wrong.')

    @staticmethod
    def __my_timer(time):
        delta_time = 0
        timer_start = perf_counter()
        while delta_time < time:
            timer_stop = perf_counter()
            delta_time = timer_stop - timer_start

my_traffic_light_1 = TrafficLight('yellow')
my_traffic_light_1.running()

my_traffic_light_2 = TrafficLight('abrakadabra')
my_traffic_light_2.running()

my_traffic_light_1 = TrafficLight()
my_traffic_light_1.running()
