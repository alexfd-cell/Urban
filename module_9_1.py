
def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        if function.__name__ == 'max':
            result[function.__name__] = max(int_list)
        if function.__name__ == 'min':
            result[function.__name__] = min(int_list)
        if function.__name__ == 'len':
            result[function.__name__] = len(int_list)
        if function.__name__ == 'sum':
            result[function.__name__] = sum(int_list)
        if function.__name__ == 'sorted':
            result[function.__name__] = sorted(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))