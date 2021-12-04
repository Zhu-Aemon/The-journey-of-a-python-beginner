# Have the user enter a number and find all Prime Factors (if there are any) and display them.
import math


def FactorFinder(n):
    li = list(filter(lambda x: n % x == 0, (int(x) for x in range(2, n - 1))))
    return li


def isPrime(n):
    li = []
    for i in range(2, n - 1):
        if n % i == 0:
            li.append(i)
    if len(li) == 0:
        return True
    else:
        return False


def PrimePrinter(n):
    li = list(filter(isPrime, FactorFinder(n)))
    return li


def main():
    print('enter a number, we will find all Prime Factors (if there are any) and display them.'
          '\nenter a q to quit.')
    while True:
        x = input('>>>')
        if x == 'q':
            break
        elif not x.isdigit():
            print('please enter a number.')
        else:
            factors = FactorFinder(int(x))
            if len(factors) == 0:
                print('no factors of this number found.')
            elif len(PrimePrinter(int(x))) == 0:
                print('no prime in the factors.')
            else:
                print('factors: ' + ' '.join(str(x) for x in PrimePrinter(int(x))))


if __name__ == '__main__':
    main()
