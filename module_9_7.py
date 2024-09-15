
def is_prime(func):
    def wrapper(a,b,c):
        res = func(a,b,c)
        d = 0
        for i in range(1, res + 1):
            if (i != 1 and res % i == 0) and (i != res and res % i == 0):
                d = 1
                break
        if d == 1:
            print('Сложное')
            return res
        else:
            print('Простое')
            return res
    return wrapper


@is_prime
def sum_three(a,b,c):
    cSum = a+b+c
    return cSum

result = sum_three(2, 3, 6)
print(result)