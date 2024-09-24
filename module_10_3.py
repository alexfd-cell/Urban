from threading import Thread, Lock
from time import sleep
from random import randint

lock = Lock()

transactions_count = 100

class Bank:
    def __init__(self):
        global balance
        self.balance = 0

    def deposit(self):
        for i in range(transactions_count):
            amount = randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if self.balance >= 500 and lock.locked():
                lock.release()
            sleep(0.001)

    def take(self):
        for i in range(transactions_count):
            amount = randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')