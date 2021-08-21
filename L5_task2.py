# 2.	Реализовать класс Road (дорога).
# ●	определить атрибуты: length (длина), width (ширина);
# ●	значения атрибутов должны передаваться при создании экземпляра класса;
# ●	атрибуты сделать защищёнными;
# ●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
# см*число см толщины полотна;
# ●	проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __specific_mass = 25.0 # kg/(m2*m)

    def __init__(self, length, width, thickness = 5):
        self._length = float(length)
        self._width = float(width)
        self._thickness = float(thickness) * 10**-2

    def mass(self):
        print(f'Mass of asphalt length: {self._length} m; width: {self._width} m; thickness: {self._thickness} m is: '
              f'{self._length*self._width*Road.__specific_mass*self._thickness} t')

road_1 = Road(5000, 20, 5)
road_1.mass()


