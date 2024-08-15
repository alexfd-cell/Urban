import math

class Figure():
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        if len(sides) == self.sides_count:
            self.__sides = [*sides]
        else:
            self.__sides = [1 for i in range(self.sides_count)]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [i for i in self.__color]

    def __is_valid_color(self, r, g, b):
        lst = [r, g, b]
        lst.sort()
        if lst[0] < 0 or lst[-1] > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        CheckSides = []
        for i in sides:
            if i > 0:
                CheckSides.append(i)
        if len(CheckSides) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides


class Circle(Figure):
    sides_count = 1

    def get_square(self, __radius):
        self.__radius = self.__len__ * (2 / pi)
        return self.__radius ** 2 * pi

class Triangle(Figure):
    sides_count = 3

    def get_square(self, __height):
        self.__height = height
        sa = self.__sides[0]  # сторона а
        sb = self.__sides[1]  # сторона b
        sc = self.__sides[2]  # сторона c
        p = self.__len__ / 2  # сие полупериметр
        ha = (2 * math.sqrt(p * (p - sa) * (p - sb) * (p - sc))) / sa  # высота к стороне а
        hb = (2 * math.sqrt(p * (p - sa) * (p - sb) * (p - sc))) / sb  # высота к стороне b
        hc = (2 * math.sqrt(p * (p - sa) * (p - sb) * (p - sc))) / sc  # высота к стороне c
        height = ha
        s = (ha * sa)/2
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1 for i in range(Cube.sides_count)]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
circle2 = Circle((200, 200, 100), 10, 7)
cube1 = Cube((222, 35, 130), 6)
cube2 = Cube((222, 35, 130), 9, 7)
tringle1 = Triangle((200, 200, 200), 10, 6, 8)
tringle2 = Triangle((100, 1500, 50), 10, 6)


print('Проверка на изменение цветов:')
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
tringle1.set_color(300, 70, 15) # Не изменится
tringle2.set_color(55, 66, 77) # Изменится
print(f'Круг1: {circle1.get_color()}')
print(f'Куб1: {cube1.get_color()}')
print(f'Треугольник1: {tringle1.get_color()}')
print(f'Треугольник2: {tringle2.get_color()}')

print('Проверка на изменение сторон:')
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
tringle1.set_sides(10, 10, 10) # Изменится
tringle2.set_sides(155, 4) # Не изменится

print(f'Куб1: {cube1.get_sides()}')
print(f'Куб2: {cube2.get_sides()}') # Изменится на 1
print(f'Круг1: {circle1.get_sides()}') # Изменится
print(f'Круг1: {circle2.get_sides()}') # Изменится на 1
print(f'Треугольник1: {tringle1.get_sides()}')
print(f'Треугольник2: {tringle2.get_sides()}') # Изменится на 1

print(f'Проверка периметра Круг1: {len(circle1)}')
print(f'Проверка объёма Куба1: {cube1.get_volume()}')
print(f'Проверка площади Круга1: {circle1.get_square}')
print(f'Проверка площади треугоьльника1: {tringle1.get_square}')