previous = {0: 0, 1: 1}


def fibonacci_s(n):
    if n in previous.keys():
        return previous[n]
    else:
        return fibonacci_s(n - 1) + fibonacci_s(n - 2)


a = int(input())
print(f'斐波那契数列第{a}项的值是：{fibonacci_s(a)}')
