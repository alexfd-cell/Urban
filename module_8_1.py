
def add_everything_up(a, b):
    try:
        c = round(a + b, 3)
    except:
        c = str(a) + str(b)
    return c


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(3.147, 6.234))
print(add_everything_up(3.147, '6.234'))