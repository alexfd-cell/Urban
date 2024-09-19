from threading import Thread
from time import sleep

enemies = 100
class Knight(Thread):
    def __init__(self, name :str, power :int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        for i in range(enemies//self.power):
            sleep(1)
            print(f'{self.name} сражается {i+1} день(дня)..., осталось {enemies-(self.power*(i+1))} воинов')
        print(f'{self.name} одержал победу спустя {enemies//self.power} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = first_knight
thread2 = second_knight
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Все битвы закончились')