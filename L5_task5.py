# 5.	Реализовать класс Stationery (канцелярская принадлежность).
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start rendering with {self.title}.')

class Pen(Stationery):
    def __init__(self):
        super().__init__(title= 'Pen')

    def draw(self):
        print(f'Start rendering with Pen {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Start rendering with Pencil {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'Start rendering with Handle {self.title}.')

new_pen = Pen()
new_pencil = Pencil('Pencil_One')
new_handle = Handle('Handle_green')

new_pen.draw()
new_pencil.draw()
new_handle.draw()