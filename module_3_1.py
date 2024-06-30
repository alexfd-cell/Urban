calls = 0
list_to_search = ['ban', 'BaNaN', 'urBAN', 'recycling', 'cyclic']
def count_calls():
    global calls
    calls += 1
def string_info(string):
    result_string_info = len(string), string.upper(), string.lower()
    count_calls()
    return result_string_info

def is_contains(string, list_to_search):
    list_to_search = list(map(str.lower, list_to_search))
    for i in range(len(list_to_search)):
        if list_to_search[i] == string.lower():
            result_is_contains = True
            break
        else:
            result_is_contains = False
    count_calls()
    return result_is_contains

n = int(input('Укажите количество строк, которые вы хотите добавить: ', )) + 1
for row_count in range(1, n):
    string = input('Введите любой текст: ', )
    result_string_info = string_info(string)
    result_is_contains = is_contains(string, list_to_search)
    print(f'Результат выполнения функции string_info: {result_string_info}')
    print(f'Результат выполнения функции is_contains: {result_is_contains}')

print(f'Количество вызовов функций = {calls}')