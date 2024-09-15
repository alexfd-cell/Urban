class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start, self.stop = start, stop
        self.step = step
        self.pointer = start - step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer == self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop:
            raise StepValueError
        if self.step < 0 and self.pointer < self.stop:
            raise StepValueError
        self.pointer += self.step
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print()

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print()

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print()