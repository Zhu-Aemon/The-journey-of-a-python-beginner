def fib(maximum):
    a, b = 1, 1
    n = 1
    while n < maximum:
        a, b = b, a + b
        n += 1
    yield a


def main():
    print('welcome to the Fibonacci Sequence generator. '
          'this generator will print the nth of the sequence. '
          'enter q to exit.'
          '\nplease input the n value')
    while True:
        x = input('>>>')
        if x == 'q':
            break
        elif not isinstance(eval(x), int):
            print('please enter an int value.')
        else:
            print(next(fib(int(x))))


if __name__ == '__main__':
    main()
