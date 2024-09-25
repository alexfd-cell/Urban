from queue import Queue
from threading import Thread
from random import randint
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.q = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.find_table()
            if table:
                table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.q.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.q.empty():
            while any(table.guest is not None for table in self.tables):
                for table in self.tables:
                    if table.guest and not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                    if not self.q.empty() and table.guest is None:
                        next_guest = self.q.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

    def find_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()