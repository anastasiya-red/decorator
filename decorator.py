def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        count = 0
        for divider in range(1, x + 1):
            res = x % divider
            if res == 0:
                count += 1
        if count <= 2:
            print('Простое')
            return func(*args)
        else:
            print('Составное')
            return func(*args)
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
