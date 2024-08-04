
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self, __model):
        self.__model

    def get_horsepower(self, __engine_power):
        self.__engine_power

    def get_color(self, __color):
        self.__color

    def print_info(self):
        print(f'Модель: {self.model}')
        print(f'Мощность двигателя: {self.engine_power}')
        print(f'Цвет: {self.color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            print(f'Произведена смена цвета с {self.color} на {new_color}')
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()