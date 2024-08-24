
def personal_sum(numbers):
    incorrect_data, result = 0, 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
    return result, incorrect_data


def personal_sum(numbers):
    incorrect_data, result = 0, 0
    try:
        for i in range(len(numbers)):
            try:
                result += numbers[i]
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        numerator = result[0]
        if len(numbers) == result[1]:
            denominator = len(numbers)
        else:
            denominator = len(numbers) - result[1]
        average = numerator/denominator
    except (ZeroDivisionError, TypeError) as exp:
        if type(exp) == TypeError:            average = None
        if type(exp) == ZeroDivisionError:            average = 0
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average("")}') # ZeroDivisionError, результат 0