# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения
# размеров, цвета и т.д. Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.

# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения
# размеров, цвета и т.д. Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.



from math import pi, sqrt

# Атрибуты класса Figure: sides_count = 0 Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB) Атрибуты(
# публичные): filled(закрашенный, bool) И методами: Метод get_color, возвращает список RGB цветов. Метод
# __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед
# установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (
# включительно). Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
# значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
# положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях. Метод get_sides
# должен возвращать значение я атрибута __sides. Метод __len__ должен возвращать периметр фигуры. Метод set_sides(
# self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
# в противном случае - менять.


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=True):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(*new_color):
        check_color = False
        for i in new_color:
            if 0 <= i <= 255:
                check_color = True
            else:
                break
        return check_color

    def set_color(self, *new_color):
        if Figure.__is_valid_color(*new_color):
            self.__color = new_color

    def __is_valid_sides (self, *new_sides):
        check_sides = True

        for x in new_sides:
            if x < 0 and type (x) is not int:
                check_sides = False

        return check_sides

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):

        if len(list(new_sides)) == self.sides_count and Figure.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides

    def __len__(self):

        if self.sides_count == 1:
            return self.__sides[0]

        if self.sides_count == 3:
            return len(range(sum(self.__sides)))

        if self.sides_count == 12:
            return len(range(sum(self.__sides)))



 # Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=True):

        self.sides = list(sides)
        if len(self.sides) == self.sides_count:
            self.sides = self.sides_count * self.sides
        else:
            self.sides = self.sides_count * [1]

        self.radius = self.sides[0]/2 * pi

        super().__init__(color, self.sides, filled)

    def get_square(self):
        s = pi * self.radius ** 2
        return s


# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=True):

        if len(list(sides)) == self.sides_count:
            self.sides = list(sides)
        else:
            self.sides = 3 * [1]

        super().__init__(color, self.sides, filled)

    def get_square(self):
        p = 0.5 * sum(self.sides)
        s = sqrt(p * (p - self.sides[1]) * (p - self.sides[2]) * (p - self.sides[3]))
        return s


# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled=True):
        self.sides = list(sides)
        if len(self.sides) == 1:
            self.sides = self.sides_count * self.sides
        else:
            self.sides = self.sides_count * [1]

        super().__init__(color, self.sides, filled)

    def get_volume(self):
        volume_cub = self.sides[1] **3
        return volume_cub


circle1 = Circle((200, 200, 100), 15)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
# circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
#Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
