# 1.Создайте функцию, которая принимает три параметра со значениями по умолчанию
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() # >>> 1 строка True
print_params(b = 25) # >>> 1 25 True
print_params(c = [1,2,3]) # >>> 1 строка [1, 2, 3]
print_params(10, 'Sunrise') # >>> 10 Sunrise True
print_params('Excel') # >>> Excel строка True
print_params(a = 0, c = False) # >>> 0 строка False
#-------------------------------------------------------

# 2.Распаковка параметров
values_list = [True, 5, 'Window']
values_dict = {'a': 7, 'b': 'August', 'c': False}
print_params(*values_list) # >>> True 5 Window
print_params(**values_dict) # >>> 7 August False

# 3.Распаковка + отдельные параметры
values_list_2 = [54.32, 'Parrot']
print_params(*values_list_2, 42) # >>> 54.32 Parrot 42
print_params('None', *values_list_2) # >>> None 54.32 Parrot